# Connections

Registry of every system your EmpathoAiOS can reach. Record confirmed connections as they are discovered; never infer credentials or access from a name alone. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Source control | GitHub — `empathoai/EMPATHOAI-OS` | git remote | configured locally; method not recorded | 2026-09-09 |
| 2 | Automation / integrations | Composio CLI `0.4.1` | WSL CLI | authenticated; org `empathoai` | 2026-09-09 |
| 3 | Web research / extraction | Firecrawl | Composio toolkit `firecrawl` | 1 active | 2026-09-09 |
| 4 | Communication | Gmail | Composio toolkit `gmail` | 3 active; 1 expired | 2026-09-09 |
| 5 | Communication | Outlook | Composio toolkit `outlook` | 1 active | 2026-09-09 |
| 6 | Content / media | YouTube | Composio toolkit `youtube` | 1 active; 1 expired | 2026-09-09 |
| 7 | Calendar / scheduling | Cal | Composio toolkit `cal` | 1 active | 2026-09-09 |
| 8 | Calendar / scheduling | Google Calendar | Composio toolkit `googlecalendar` | 1 expired; re-link required | 2026-09-09 |
| 9 | Calendar / scheduling | Google Meet | Composio toolkit `googlemeet` | 1 active | 2026-09-09 |
| 10 | Project / task tracking | Google Tasks | Composio toolkit `googletasks` | 1 active; 1 expired | 2026-09-09 |
| 11 | Knowledge / files | Google Drive | Composio toolkit `googledrive` | 1 active; 1 expired | 2026-09-09 |
| 12 | Knowledge / files | Google Docs | Composio toolkit `googledocs` | 1 active | 2026-09-09 |
| 13 | Knowledge / files | Google Sheets | Composio toolkit `googlesheets` | 1 active | 2026-09-09 |
| 14 | Customer / data operations | Airtable | Composio toolkit `airtable` | 1 active; 1 failed | 2026-09-09 |
| 15 | Search / analytics | Google Search Console | Composio toolkit `google_search_console` | 1 active | 2026-09-09 |
| 16 | Web automation / extraction | Apify | Composio toolkit `apify` | 1 active; 1 expired | 2026-09-09 |
| 17 | Revenue / Financials | _not recorded_ | not yet connected | — | — |
| 18 | Customer interactions | _not recorded_ | not yet connected | — | — |
| 19 | Project / task tracking | _not recorded_ | not yet connected | — | — |
| 20 | Meeting intelligence | _not recorded_ | not yet connected | — | — |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `git remote`, `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever. Composio-specific usage is documented in `references/composio-cli.md`.

## Composio capability coverage

These are confirmed operational uses of the currently available Composio toolkits. Availability of a toolkit does not authorize an action; execution still requires an active account, validated inputs, and explicit scope for side effects.

| OS area | Toolkit | Useful for | Current status |
|---|---|---|---|
| Communication | `gmail` | Search and retrieve email, organize labels, draft or send messages, and process mailbox workflows | Active accounts available |
| Communication | `outlook` | Read and manage Outlook email and calendar events | Active account available |
| Content and distribution | `youtube` | Inspect channel/video data, organize playlists, and support content operations | Active account available |
| Calendar and scheduling | `cal` | Review bookings, availability, attendees, and scheduling operations | Active account available |
| Calendar and scheduling | `googlecalendar` | Manage Google Calendar events and schedules | Connection expired; re-link required |
| Meetings | `googlemeet` | Create and inspect meeting spaces and manage meeting operations | Active account available |
| Task management | `googletasks` | Read, create, update, and organize task lists | Active account available |
| Knowledge and files | `googledrive` | Search and manage files, folders, sharing, and permissions | Active account available; one expired record also exists |
| Knowledge and documents | `googledocs` | Copy, create, populate, and manage Google Documents | Active account available |
| Knowledge and data | `googlesheets` | Read and update spreadsheet data and sheets | Active account available |
| Structured operations | `airtable` | Manage bases, records, comments, and structured operational data | Active account available; one failed record also exists |
| Marketing measurement | `google_search_console` | Inspect sites, search performance, and SEO-related analytics | Active account available |
| Web research and extraction | `apify` | Run and manage actors for web automation and data extraction | Active account available; one expired record also exists |

### Practical OS uses

- **Lead and client operations:** search communications, organize follow-ups, manage structured records, and prepare meeting or booking workflows.
- **Content operations:** research or extract web data, inspect YouTube performance, and coordinate content assets in Drive, Docs, and Sheets.
- **Delivery management:** turn commitments into Google Tasks, track operational data in Airtable or Sheets, and coordinate meetings through Cal or Google Meet.
- **Marketing measurement:** review Search Console data and connect findings to content, pipeline, and decision reviews.
- **Knowledge management:** locate source material in Drive, maintain documents, and use Sheets or Airtable as structured operational indexes.

These are capability mappings, not approved automations. Each workflow must first be defined and tested manually, then automated only when the expected evidence and safeguards are clear.
