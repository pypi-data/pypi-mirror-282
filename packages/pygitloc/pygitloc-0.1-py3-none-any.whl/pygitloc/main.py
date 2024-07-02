import os
import sys
import subprocess
from git import Repo
from github import Github

def clone_repo(github_link, clone_dir):
    try:
        Repo.clone_from(github_link, clone_dir)
        print(f"Cloned {github_link} to {clone_dir}")
    except Exception as e:
        print(f"Error cloning repo: {e}")
        sys.exit(1)

def count_loc(clone_dir):
    try:
        result = subprocess.run(['cloc', clone_dir], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except Exception as e:
        print(f"Error counting lines of code: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: pygitloc <github-link>")
        sys.exit(1)

    github_link = sys.argv[1]
    clone_dir = 'temp_repo'

    clone_repo(github_link, clone_dir)
    count_loc(clone_dir)

    # Clean up
    try:
        subprocess.run(['rm', '-rf', clone_dir])
    except Exception as e:
        print(f"Error removing temp directory: {e}")

if __name__ == "__main__":
    main()
