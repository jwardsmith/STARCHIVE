#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
import csv
import requests

# === EMBEDDED CREDENTIALS AND OUTPUT PATH ===
GITHUB_USERNAME = "<your_username>"
GITHUB_TOKEN = "<your_personal_access_token>"
OUTPUT_CSV = "starred_repo_lists.csv"  # Change if you want to customise output path


class Starchive:
    def __init__(self):
        self.username = GITHUB_USERNAME
        self.token = GITHUB_TOKEN
        self.output_csv = OUTPUT_CSV
        self.star_lists = []        # list of tuples: (list_slug, list_name)
        self.star_list_repos = {}   # dict: list_slug -> list of (owner, repo)
        self.data = {}              # dict: full_name -> repo info

        if not self.username or not self.token:
            raise ValueError("GITHUB_USERNAME and GITHUB_TOKEN must be set in the script")

    def get_all_starred(self):
        url = f"https://api.github.com/users/{self.username}/starred?per_page=100"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Starchive",
        }
        all_repos = {}
        while url:
            print(f"Fetching starred repos page: {url}")
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            for repo in response.json():
                all_repos[repo["full_name"]] = {
                    "html_url": repo["html_url"],
                    "description": repo["description"] or "",
                    "listed": False,
                    "stars": repo["stargazers_count"],
                }
            url = response.links.get("next", {}).get("url")
        self.data = all_repos
        print(f"Total starred repos fetched: {len(self.data)}")
        return all_repos

    def get_lists(self):
        url = f"https://github.com/{self.username}?tab=stars"
        print(f"Fetching starred lists from: {url}")
        response = requests.get(url)
        pattern = f'href="/stars/{self.username}/lists/(\\S+)".*?<h3 class="f4 text-bold no-wrap mr-3">(.*?)</h3>'
        match = re.findall(pattern, response.text, re.DOTALL)
        self.star_lists = [(slug, name.strip()) for slug, name in match]
        print(f"Starred lists found: {self.star_lists}")
        return self.star_lists

    def get_list_repos(self, list_slug):
        url_template = "https://github.com/stars/{username}/lists/{list_slug}?page={page}"
        page = 1
        repos_in_list = []
        while True:
            current_url = url_template.format(
                username=self.username, list_slug=list_slug, page=page
            )
            print(f"Fetching list '{list_slug}' repos page {page}: {current_url}")
            response = requests.get(current_url)
            pattern = r'<h3>\s*<a href="[^"]*">\s*<span class="text-normal">(\S+) / </span>(\S+)\s*</a>\s*</h3>'
            match = re.findall(pattern, response.text)
            if not match:
                break
            repos_in_list.extend(match)
            page += 1
        self.star_list_repos[list_slug] = repos_in_list
        print(f"Repos found in list '{list_slug}': {len(repos_in_list)}")
        return repos_in_list

    def get_all_repos(self):
        if not self.star_lists:
            print("No starred lists found, assigning all repos to 'All Starred'")
            all_repos = [(full_name.split('/')[0], full_name.split('/')[1]) for full_name in self.data]
            self.star_lists = [("all_starred", "All Starred")]
            self.star_list_repos["all_starred"] = all_repos
            for full_name in self.data:
                self.data[full_name]["listed"] = True
            return self.star_list_repos

        for list_slug, _ in self.star_lists:
            self.get_list_repos(list_slug)
            for owner, repo in self.star_list_repos[list_slug]:
                full_name = f"{owner}/{repo}"
                if full_name in self.data:
                    self.data[full_name]["listed"] = True
        return self.star_list_repos

    def export_csv(self):
        print(f"Exporting starred repos to CSV: {self.output_csv}")
        with open(self.output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["repo_full_name", "repo_url", "description", "stars", "list_name"])
            for list_slug, list_name in self.star_lists:
                repos = self.star_list_repos.get(list_slug, [])
                for owner, repo in repos:
                    full_name = f"{owner}/{repo}"
                    if full_name in self.data:
                        info = self.data[full_name]
                        writer.writerow([
                            full_name,
                            info["html_url"],
                            info["description"].replace("\n", " ").replace("\t", " "),
                            info["stars"],
                            list_name,
                        ])
            uncategorised = [k for k, v in self.data.items() if not v["listed"]]
            if uncategorised:
                for full_name in uncategorised:
                    info = self.data[full_name]
                    writer.writerow([
                        full_name,
                        info["html_url"],
                        info["description"].replace("\n", " ").replace("\t", " "),
                        info["stars"],
                        "Uncategorised",
                    ])
        print("CSV export completed.")


if __name__ == "__main__":
    starchive = Starchive()
    starchive.get_all_starred()
    starchive.get_lists()
    starchive.get_all_repos()
    starchive.export_csv()
