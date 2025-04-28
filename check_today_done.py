import os
import json
import datetime
import subprocess

SOLUTIONS_DIR = "/home/arataka/leetcode/solutions"
STREAK_FILE = "/home/arataka/leetcode/streak.json"
DISCORD_SCRIPT = "/home/arataka/leetcode/reminder/send_discord.py"

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

def load_streak():
    if not os.path.exists(STREAK_FILE):
        return {
            "current_streak": 0,
            "max_streak": 0,
            "last_checked_date": None
        }
    with open(STREAK_FILE, "r") as f:
        return json.load(f)

def save_streak(streak_data):
    with open(STREAK_FILE, "w") as f:
        json.dump(streak_data, f, indent=4)

def update_streak(did_update_today):
    today_str = datetime.date.today().isoformat()
    streak = load_streak()

    if streak["last_checked_date"] == today_str:
        return

    if did_update_today:
        streak["current_streak"] += 1
        if streak["current_streak"] > streak["max_streak"]:
            streak["max_streak"] = streak["current_streak"]
        print(f"LeetCodeやったね!現在の連続達成日数: {streak['current_streak']}日")
    else:
        print(f"今日はLeetCodeやってないよ…ストリークリセット。")
        streak["current_streak"] = 0

    streak["last_checked_date"] = today_str
    save_streak(streak)

def main():
    did_update_today = is_today_updated(SOLUTIONS_DIR)
    update_streak(did_update_today)

    if not did_update_today:
        subprocess.run(["python3", DISCORD_SCRIPT])

if __name__ == "__main__":
    main()
