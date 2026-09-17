[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ManifestPath,
    [switch]$AsJson
)

$ErrorActionPreference = 'Stop'
$allowedStatuses = @('PASS', 'PARTIAL', 'BLOCKED', 'NOT RUN')
$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

if (-not (Test-Path -LiteralPath $ManifestPath -PathType Leaf)) {
    $errors.Add("Manifest not found: $ManifestPath")
} else {
    try { $manifest = Get-Content -LiteralPath $ManifestPath -Raw -Encoding UTF8 | ConvertFrom-Json }
    catch { $errors.Add("Manifest is not valid JSON: $($_.Exception.Message)") }
}

if ($null -ne $manifest) {
    if ($null -eq $manifest.audit_id -or [string]::IsNullOrWhiteSpace([string]$manifest.audit_id)) { $errors.Add('Missing audit_id') }
    if ($null -eq $manifest.phases -or @($manifest.phases).Count -eq 0) { $errors.Add('Manifest must contain phases') }
    if ($null -eq $manifest.required_phase_ids -or @($manifest.required_phase_ids).Count -eq 0) {
        $errors.Add('Manifest must declare required_phase_ids')
    } else {
        $present = @($manifest.phases | ForEach-Object { [string]$_.id })
        foreach ($requiredId in @($manifest.required_phase_ids)) {
            $requiredIdText = [string]$requiredId
            if ($present -notcontains $requiredIdText) {
                $errors.Add("Required phase missing: $requiredIdText")
            } else {
                $requiredPhase = @($manifest.phases | Where-Object { [string]$_.id -eq $requiredIdText }) | Select-Object -First 1
                if ([string]$requiredPhase.status -ne 'PASS') {
                    $errors.Add("Required phase is not PASS: $requiredIdText ($($requiredPhase.status))")
                }
            }
        }
    }

    foreach ($phase in @($manifest.phases)) {
        $id = [string]$phase.id
        if ([string]::IsNullOrWhiteSpace($id)) { $errors.Add('A phase is missing id'); continue }
        $status = [string]$phase.status
        if ($allowedStatuses -notcontains $status) { $errors.Add("$id has invalid status '$status'") }
        if ($phase.mandatory -eq $true -and $status -ne 'PASS') {
            $errors.Add("Mandatory phase is not PASS: $id ($status)")
        }
        if ($status -eq 'PASS') {
            if ($phase.minimum_analysis_complete -ne $true) { $errors.Add("PASS phase lacks minimum_analysis_complete=true: $id") }
            if ($null -eq $phase.coverage -or [string]::IsNullOrWhiteSpace([string]$phase.coverage)) { $errors.Add("PASS phase lacks coverage: $id") }
            $artifact = [string]$phase.artifact_path
            if ($phase.required_artifact -eq $true) {
                if ([string]::IsNullOrWhiteSpace($artifact)) { $errors.Add("PASS phase lacks required artifact_path: $id") }
                elseif (-not (Test-Path -LiteralPath $artifact -PathType Leaf)) { $errors.Add("Required artifact not found for $id`: $artifact") }
                elseif ($phase.sha256) {
                    $actual = (Get-FileHash -LiteralPath $artifact -Algorithm SHA256).Hash
                    if ($actual.ToUpperInvariant() -ne ([string]$phase.sha256).ToUpperInvariant()) { $errors.Add("Artifact hash mismatch for $id") }
                }
            }
        } elseif ([string]::IsNullOrWhiteSpace([string]$phase.limitation)) {
            $warnings.Add("Non-PASS phase should document limitation/recovery: $id")
        }
    }

    $review = @($manifest.phases | Where-Object { [string]$_.id -in @('FASE 8','review-intelligence','reviews') }) | Select-Object -First 1
    if ($null -eq $review) { $errors.Add('Missing mandatory review-intelligence phase') }
    elseif ($review.status -eq 'PASS') {
        foreach ($field in @('dataset_coverage','rating_1_to_4_count','repeated_themes','owner_response_analysis','unresolved_issues')) {
            if ($null -eq $review.$field -or ([string]::IsNullOrWhiteSpace([string]$review.$field) -and $review.$field -is [string])) { $errors.Add("Review intelligence missing: $field") }
        }
    }
    if ($null -eq $manifest.evidence_manifest -or @($manifest.evidence_manifest).Count -eq 0) { $errors.Add('Missing evidence_manifest records') }
}

$result = [ordered]@{
    audit_id = if ($manifest) { $manifest.audit_id } else { $null }
    can_complete = ($errors.Count -eq 0)
    recommended_status = if ($errors.Count -eq 0) { 'COMPLETE' } elseif ($manifest -and @($manifest.phases | Where-Object status -eq 'BLOCKED').Count -gt 0) { 'BLOCKED' } else { 'PARTIAL' }
    errors = @($errors)
    warnings = @($warnings)
}
if ($AsJson) { $result | ConvertTo-Json -Depth 8; if (-not $result.can_complete) { exit 1 }; exit 0 }
Write-Output ("Prospect audit manifest: {0} | {1}" -f $result.recommended_status, $result.audit_id)
@($errors) | ForEach-Object { Write-Output "ERROR: $_" }
@($warnings) | ForEach-Object { Write-Output "WARNING: $_" }
if (-not $result.can_complete) { exit 1 }
