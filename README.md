# STARCHIVE

**STARCHIVE** is a toolset for collecting, organising, and exporting your GitHub starred repositories. Whether you're saving projects for inspiration, research, or tracking tools, STARCHIVE turns stars into structured data — and even recognizes starred **Lists**.

---

### Features

- Fetch all your GitHub starred repositories
- Detect stars in GitHub Lists and categorise (if used)
- Export structured CSV files with metadata like:
  - Repository name and URL
  - Description and language
  - Star count
  - List assignment (or "Uncategorised")
- Supports both **PowerShell + GitHub CLI** and **Python + GitHub API**
- Great for automation, backups, dashboards, or analysis

---

## Output Examples

### `starred_repos.csv` (PowerShell script)

| full\_name            | description | html\_url                                                                        | language | stars | forks | created\_at | updated\_at |
| --------------------- | ----------- | -------------------------------------------------------------------------------- | -------- | ----- | ----- | ----------- | ----------- |
| `gentilkiwi/mimikatz` | A little tool to play with Windows security | [https://github.com/gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz) | C     | 20186  | 3873   | 2014-04-06T18:30:02Z         | 2025-05-18T10:01:59Z         |

### `starred_repo_lists.csv` (Python script)

| repo\_full\_name | repo\_url                                                              | description     | stars | list\_name     |
| ---------------- | ---------------------------------------------------------------------- | --------------- | ----- | -------------- |
| `PowerShellMafia/PowerSploit`   | [https://github.com/PowerShellMafia/PowerSploit](https://github.com/PowerShellMafia/PowerSploit)     | PowerSploit - A PowerShell Post-Exploitation Framework        | 12325  | Active Directory   |
| `redcanaryco/atomic-red-team` | [https://github.com/redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) | Small and highly portable detection tests based on MITRE's ATT&CK. | 10561 | Adversary Emulation |

---

## Installation

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/starchive.git
cd starchive
```

---

## PowerShell Usage (Requires GitHub CLI)

### Requirements:

* [GitHub CLI](https://cli.github.com/) installed and authenticated (`gh auth login`)

### Run:

```powershell
.\Get-StarredRepos.ps1
```

This will output `starred_repos.csv`.

---

## Python Usage (Categorised Lists)

### Requirements:

* `requests` installed (`pip install requests`)

### Set credentials in the script:

Edit `StarredRepoLists.py` and set:

```python
GITHUB_USERNAME = "<your_username>"
GITHUB_TOKEN = "<your_personal_access_token>"
```

### Run:

```bash
python StarredRepoLists.py
```

This will output `starred_repo_lists.csv`.

---

## Notes

* The **GitHub token** must have `public_repo` scope.
* Lists are a feature on GitHub Stars UI — [example here](https://github.com/stars/jwardsmith/lists).
* STARCHIVE is read-only — it **does not modify** any of your GitHub data.

---

## Inspired by

* GitHub CLI (`gh api`)
* GitHub’s new "Starred Lists"
* Manual pain of organising stars

---
