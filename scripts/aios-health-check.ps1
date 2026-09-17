# AIOS Automated Health & Cadence Check
$dateStr = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
$logPath = "F:\EMPATHOAI_OS\audits\cadence.log"
$status = "OK"
$details = @()

# 1. Check SSOT and Read-Only OS roots
$checks = @(
    @{ Name = "EmpathoKnowledge SSOT"; Path = "F:\EmpathoKnowledge" },
    @{ Name = "OS-MarketingHub"; Path = "F:\OS-MarketingHub" },
    @{ Name = "OS-WebInteligence"; Path = "F:\OS-WebInteligence" },
    @{ Name = "Audits Directory"; Path = "F:\EMPATHOAI_OS\audits" },
    @{ Name = "Decisions Log"; Path = "F:\EMPATHOAI_OS\decisions\log.md" }
)

foreach ($c in $checks) {
    if (Test-Path $c.Path) {
        $details += "[$($c.Name)]: OK"
    } else {
        $details += "[$($c.Name)]: MISSING ($($c.Path))"
        $status = "WARN"
    }
}

$logEntry = "[$dateStr] Status: $status | " + ($details -join " | ")
Add-Content -LiteralPath $logPath -Value $logEntry -Encoding UTF8
Write-Output $logEntry
