# Check if GitHub CLI is installed
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "GitHub CLI (gh) is not installed. Please install it from https://cli.github.com/."
    exit 1
}

# Check authentication status
$authStatus = & gh auth status 2>&1

if ($authStatus -like "*You are not logged into any GitHub hosts*") {
    Write-Host "You are not authenticated with GitHub. Logging in..."
    & gh auth login
} else {
    Write-Host "GitHub authentication already set up."
}

# Fetch starred repos using GitHub CLI, parse JSON, convert to CSV
Write-Host "Fetching starred repositories..."

$json = & gh api user/starred --paginate | ConvertFrom-Json

if ($json) {
    $csvData = $json | Select-Object `
        full_name,
        description,
        html_url,
        language,
        stargazers_count,
        forks_count,
        created_at,
        updated_at

    $csvData | Export-Csv -Path "starred_repos.csv" -NoTypeInformation -Encoding UTF8
    Write-Host "Saved starred repositories to starred_repos.csv"
} else {
    Write-Host "No starred repositories found or failed to fetch them."
}