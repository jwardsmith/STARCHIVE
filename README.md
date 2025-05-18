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
  - List assignment (or "Uncategorized")
- Supports both **PowerShell + GitHub CLI** and **Python + GitHub API**
- Great for automation, backups, dashboards, or analysis

---

## Output Examples

### `starred_repos.csv` (PowerShell script)

| full\_name            | description | html\_url                                                                        | language | stars | forks | created\_at | updated\_at |
| --------------------- | ----------- | -------------------------------------------------------------------------------- | -------- | ----- | ----- | ----------- | ----------- |
| `octocat/Hello-World` | Sample repo | [https://github.com/octocat/Hello-World](https://github.com/octocat/Hello-World) | Ruby     | 1520  | 600   | ...         | ...         |

### `starred_repo_lists.csv` (Python script)

| repo\_full\_name | repo\_url                                                              | description     | stars | list\_name     |
| ---------------- | ---------------------------------------------------------------------- | --------------- | ----- | -------------- |
| `psf/requests`   | [https://github.com/psf/requests](https://github.com/psf/requests)     | HTTP lib        | 50k+  | Python Tools   |
| `vercel/next.js` | [https://github.com/vercel/next.js](https://github.com/vercel/next.js) | React framework | 110k+ | Web Frameworks |

---

## ⚙Installation

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/starchive.git
cd starchive
```

---

## PowerShell Usage (Requires GitHub CLI)

### Requirements:

* PowerShell 5.1+
* [GitHub CLI](https://cli.github.com/) installed and authenticated (`gh auth login`)

### Run:

```powershell
.\Get-StarredRepos.ps1
```

This will output `starred_repos.csv`.

---

## Python Usage (Categorized Lists)

### Requirements:

* Python 3.7+
* `requests` installed (`pip install requests`)

### Set credentials in the script:

Edit `StarredRepoLists.py` and set:

```python
GITHUB_USERNAME = "your_username"
GITHUB_TOKEN = "your_personal_access_token"
```

### Run:

```bash
python StarredRepoLists.py
```

This will output `starred_repo_lists.csv`.

---

## Notes

* The **GitHub token** must have `public_repo` scope.
* Lists are a feature on GitHub Stars UI — [example here](https://github.com/stars/YOUR_USERNAME/lists).
* STARCHIVE is read-only — it **does not modify** any of your GitHub data.

---

## Inspired by

* GitHub CLI (`gh api`)
* GitHub’s new "Starred Lists"
* Manual pain of organizing stars

---
