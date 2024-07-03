import os
import sys
from git import Repo

def clone_repo(github_link, clone_dir):
    try:
        Repo.clone_from(github_link, clone_dir)
        print(f"Cloned {github_link} to {clone_dir}")
    except Exception as e:
        print(f"Error cloning repo: {e}")
        sys.exit(1)

def count_lines_of_code(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.java', '.cpp', '.c', '.h', '.html', '.css', '.go', '.rb', '.php', '.ts', '.swift')):  # Add more extensions as needed
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        total_lines += len(lines)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return total_lines

def main():
    if len(sys.argv) != 2:
        print("Usage: pygitloc <github-link>")
        sys.exit(1)

    github_link = sys.argv[1]
    clone_dir = 'temp_repo'

    clone_repo(github_link, clone_dir)
    total_lines = count_lines_of_code(clone_dir)
    print(f"Total lines of code: {total_lines}")

    # Clean up
    try:
        if os.name == 'nt':
            os.system(f'rmdir /S /Q {clone_dir}')
        else:
            os.system(f'rm -rf {clone_dir}')
    except Exception as e:
        print(f"Error removing temp directory: {e}")

if __name__ == "__main__":
    main()