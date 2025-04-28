import os
from dotenv import load_dotenv
import requests
from datetime import datetime

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_reminder():
    if not webhook_url:
        print("Webhook URLが設定されていません!.envファイルを確認してください。")
        return
    
    message = {
        "content": f"📢 {datetime.now().strftime('%Y-%m-%d')} 今日のLeetCodeがまだアップされてないよ!🌱急げ!"
    }

    try:
        response = requests.post(webhook_url, json=message)
        if response.status_code == 204:
            print("Discordに正常に通知を送信しました。")
        else:
            print(f"通知送信に失敗しました。ステータスコード: {response.status_code}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    send_discord_reminder()
