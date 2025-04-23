import requests
from datetime import datetime

def send_discord_reminder():
    webhook_url = "https://discord.com/api/webhooks/XXXXXX/XXXXXX"  # 自分のWebhook URLに置き換えてね！
    message = {
        "content": f"{datetime.now().strftime('%Y-%m-%d')} 今日のLeetCodeがまだアップされてないよ！草を守れ！🌿"
    }
    response = requests.post(webhook_url, json=message)
    print("Discordに通知を送信しました。", response.status_code)

if __name__ == "__main__":
    send_discord_reminder()
