\# Lost Paths



\*\*Keep the reasoning behind experiments, not just their outcomes.\*\*



Lost Paths is a small, local-first Python CLI for recording experiments, failed approaches, abandoned ideas, and the evidence behind each decision.



The goal is simple: make it easier to remember what you tried, what happened, and why you chose not to continue.



\## Requirements



\- Python 3.9 or newer

\- No third-party dependencies



\## Quick start



Run commands from the repository root.



\### Record an experiment



```powershell

python .\\lost-paths\\lost\_paths.py add --title "Cache strategy" --idea "Try an in-memory cache" --outcome abandoned --reason "Memory use grew too quickly" --evidence "Observed during local testing"

```



Available outcomes: `success`, `failed`, `abandoned`, `inconclusive`.



\### List experiments



```powershell

python .\\lost-paths\\lost\_paths.py list

```



Filter by outcome:



```powershell

python .\\lost-paths\\lost\_paths.py list --outcome failed

```



\### Search experiment history



```powershell

python .\\lost-paths\\lost\_paths.py search cache

```



Search checks the title, idea, outcome, reason, and evidence fields.



\### View outcome statistics



```powershell

python .\\lost-paths\\lost\_paths.py stats

```



\## Data and privacy



Records are stored locally in `experiments.json` beside the script. The tool does not send experiment data to a server.



Back up your records before editing them manually. Keep private or sensitive information out of experiment notes before sharing the repository.



\## Current scope



Lost Paths is an early-stage CLI. It records and searches decisions; it does not automatically evaluate experiments or determine which approach is best.
