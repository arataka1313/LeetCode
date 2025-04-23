import os
import datetime
import subprocess

def is_today_updated(root_path):
    today = datetime.date.today()
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                mtime = datetime.date.fromtimestamp(os.path.getmtime(filepath))
                if mtime == today:
                    return True
            except Exception:
                continue
    return False

if __name__ == "__main__":
    ROOT = "/home/arataka/leetcode/solutions"
    if is_today_updated(ROOT):
        print("✅ 今日の分、確認できました！")
    else:
        print("🚨 LeetCode解いてないよ！Discordに通知します！")
        subprocess.run(["python3", "/home/arataka/leetcode/reminder/send_discord.py"])
