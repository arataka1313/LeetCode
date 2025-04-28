# LeetCode Grass Reminder

This project helps maintain daily LeetCode solving habits by automatically checking for updates and sending reminder notifications if needed.

## Features

- Organized LeetCode solutions under `/solutions`
- Automatic tracking of current and maximum streaks
- Daily reminder notifications via Discord Webhook
- Easy GitHub push for daily commits (grass farming)
- Environment variables management (.env support)

## How It Works

1. Solve a LeetCode problem and save it under `/solutions/{problem_number}/`.
2. After solving, upload the solutions to the remote server (e.g., using `scp`).
3. The remote server automatically runs `check_today_done.py` every night at 9 PM (via cron).
4. If no solution is found for today, a reminder is sent to Discord.

## Setup Instructions

1. Clone this repository.
2. Install the required Python packages:
    ```
    pip install requests python-dotenv
    ```
3. Create a `.env` file in the project root:
    ```
    DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_url
    ```
4. Create an initial `streak.json` file:
    ```json
    {
      "current_streak": 0,
      "max_streak": 0,
      "last_checked_date": null
    }
    ```
5. Set up a daily cron job to run `check_today_done.py` at 9 PM.

## Example Cron Setup

Edit crontab:
```bash
crontab -e
