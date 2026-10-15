import sys
import requests

URL = "https://api.github.com/repos/Nevan-Jose/devops-learning"

def fetch_repo_status():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        print("--- REPOSITORY METRICS ---")
        print(f"Repo Name:      {data.get('name')}")
        print(f"Default Branch: {data.get('default_branch')}")
        print(f"Open Issues:    {data.get('open_issues_count')}")
        print(f"Stars:          {data.get('stargazers_count')}")
        print("--------------------------")

    except requests.exceptions.RequestException as err:
        print(f"CRITICAL: API Request failed: {err}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_repo_status()
