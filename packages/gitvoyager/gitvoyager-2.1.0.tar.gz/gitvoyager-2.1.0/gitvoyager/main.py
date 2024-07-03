import os
import requests
import webbrowser
import platform
import subprocess
import argparse

TOKEN_FILE = 'token.tkn'


def get_github_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            token = f.read().strip()
        print("GitHub token read from token.tkn file.")
    else:
        print("GitHub token not found in token.tkn file.")
        print("Please follow these steps to generate a personal access token:")
        print("1. Open the following URL: https://github.com/settings/tokens")
        print("2. Click on 'Generate new token'.")
        print("3. Provide a note for your token (e.g., 'My Script Token').")
        print("4. Select scopes for the token (e.g., 'repo' for repository access).")
        print("5. Click 'Generate token' at the bottom of the page.")
        print("6. Copy the generated token.")

        token_url = "https://github.com/settings/tokens"
        webbrowser.open(token_url)

        token = input("Enter your GitHub personal access token: ")

        with open(TOKEN_FILE, 'w') as f:
            f.write(token)
        print("Token saved to token.tkn file.")

    return token


def search_github_repo(repo_name, token):
    url = f"https://api.github.com/search/repositories?q={repo_name}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.json().get('message')}")
        return None


def display_repositories(repos):
    if 'items' in repos:
        for i, repo in enumerate(repos['items'], start=1):
            print(f"{i}. {repo['full_name']} (Stars: {repo['stargazers_count']})")
            print(f"   URL: {repo['html_url']}\n")
    else:
        print("No repositories found.")


def clone_repository(repo_url):
    try:
        desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
        repo_name = repo_url.split('/')[-1].split('.')[0]
        destination_path = os.path.join(desktop_dir, repo_name)
        subprocess.run(['git', 'clone', repo_url, destination_path], check=True)
        print(f"Repository {repo_url} cloned successfully to {destination_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")


def main():
    parser = argparse.ArgumentParser(description="GitHub repository search and clone tool")
    subparsers = parser.add_subparsers(dest="command")

    clone_parser = subparsers.add_parser("clone", help="Clone a GitHub repository")
    clone_parser.add_argument("repo_name", type=str, help="Name of the repository to search and clone")

    args = parser.parse_args()

    if args.command == "clone":
        token = get_github_token()
        repos = search_github_repo(args.repo_name, token)

        if repos:
            display_repositories(repos)
            repo_number = int(input("Enter the number of the repository to clone: "))
            selected_repo = repos['items'][repo_number - 1]
            clone_repository(selected_repo['clone_url'])
        else:
            print("Error fetching repositories from GitHub.")


if __name__ == "__main__":
    main()
