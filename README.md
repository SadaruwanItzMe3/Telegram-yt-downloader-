
# YouTube Downloader Telegram Bot

This bot allows users to download YouTube videos and audio directly through Telegram. It's fast, reliable, and simple to use.

## Features
- Download YouTube videos in MP4 format
- Download YouTube audio in MP3 format
- Simple commands for seamless user experience

## Commands
- `/start` - Introduction and instructions
- `/video <url>` - Download video from provided URL
- `/audio <url>` - Download audio from provided URL

## Installation
1. Clone the repository:
   ```
   git clone <repo_link>
   cd <repo_folder>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your bot token in `config.yaml`:
   ```yaml
   BOT_TOKEN: 'YOUR_TELEGRAM_BOT_TOKEN'
   ```
4. Run the bot:
   ```
   python bot.py
   ```

## Hosting Options
- [Replit](https://replit.com/) (Recommended for simplicity)
- [Heroku](https://www.heroku.com/) (For stable deployment)
- [Railway](https://railway.app/) (For modern deployment)

## Dependencies
- `python-telegram-bot`
- `yt-dlp`

## License
MIT License
