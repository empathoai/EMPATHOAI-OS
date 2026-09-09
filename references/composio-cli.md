# Composio CLI

## Confirmed environment

- CLI version: `0.4.1`
- Runtime: WSL / Ubuntu on Windows
- Account verified with `composio whoami`
- Organization: `empathoai`
- Authentication state is managed outside the repository by Composio under `~/.composio/`
- Do not copy tokens, user data, or connection secrets into this repository.

## Standard usage

1. Discover a use case:

   ```bash
   composio search "<use case>" --limit 5
   ```

2. Inspect the selected tool and schema:

   ```bash
   composio tools info <TOOL_SLUG>
   composio execute <TOOL_SLUG> --get-schema
   ```

3. Check the connected account before execution:

   ```bash
   composio connections list
   ```

4. Execute only after confirming the account, inputs, and side-effect level:

   ```bash
   composio execute <TOOL_SLUG> -d '{ ... }'
   ```

5. Link or re-link a toolkit when no active account exists:

   ```bash
   composio link <toolkit>
   ```

Use `--dry-run` where supported to validate inputs without performing the external action. Prefer read-only tools for discovery and validation. Treat create, update, delete, send, publish, permission, and batch tools as side-effecting and require explicit scope before execution.

## Confirmed active toolkits

The following toolkits had at least one `ACTIVE` account and returned tools successfully through `composio tools list --limit 3`:

- `gmail` — email search, retrieval, labeling, and message operations
- `youtube` — video and channel operations
- `googletasks` — task-list and task operations
- `cal` — booking and scheduling operations
- `google_search_console` — site and search-performance operations
- `googledrive` — file and permission operations
- `googlemeet` — meeting-space operations
- `googledocs` — document operations
- `airtable` — bases, records, and comments
- `outlook` — email and calendar operations
- `googlesheets` — spreadsheet and sheet operations
- `apify` — actor and web-automation operations

Composio search returned a usable result for representative read-oriented use cases across all twelve active toolkits: listing emails, videos, tasks, bookings, search analytics, files, meeting spaces, documents, records, calendar events, spreadsheet values, and actors.

## Current account status

- Active: Gmail (3), YouTube (1), Google Tasks (1), Cal (1), Google Search Console (1), Google Drive (1), Google Meet (1), Google Docs (1), Airtable (1), Outlook (1), Google Sheets (1), Apify (1).
- Expired: Gmail (1), YouTube (1), Google Calendar (1), Google Tasks (1), Google Drive (1), Apify (1), Square (1), WhatsApp (1), Facebook (1).
- Failed: Airtable (1).

These counts describe Composio connection records at the time of inspection, not verified ownership or current data freshness.
