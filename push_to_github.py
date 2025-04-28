import os
import subprocess
from datetime import datetime

def push_to_github():
    repo_path = os.path.expanduser("~/LeetCode")
    os.chdir(repo_path)

    try:
        subprocess.run(["git", "add", "."], check=True)
        
        today = datetime.now().strftime("%Y-%m-%d")
        commit_message = f"LeetCode update: {today}"

        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print(f"itHubにpushしました!メッセージ: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"エラー発生!: {e}")

if __name__ == "__main__":
    push_to_github()
