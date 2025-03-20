
import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Load token from config.yaml
import yaml
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

TOKEN = config.get("BOT_TOKEN")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome to the YouTube Downloader Bot!\n"
                                    "Use /video <url> for video download\n"
                                    "Use /audio <url> for audio download")

async def download_video(update: Update, context: CallbackContext) -> None:
    url = context.args[0] if context.args else None
    if not url:
        await update.message.reply_text("Please provide a valid YouTube URL.")
        return

    await update.message.reply_text("Downloading video...")

    output_path = "downloads/"
    os.makedirs(output_path, exist_ok=True)

    try:
        with yt_dlp.YoutubeDL({'format': 'bestvideo+bestaudio/best',
                               'outtmpl': f'{output_path}%(title)s.%(ext)s'}) as ydl:
            ydl.download([url])

        video_file = max(os.listdir(output_path), key=lambda x: os.path.getctime(os.path.join(output_path, x)))
        await update.message.reply_video(video=open(os.path.join(output_path, video_file), 'rb'))
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

async def download_audio(update: Update, context: CallbackContext) -> None:
    url = context.args[0] if context.args else None
    if not url:
        await update.message.reply_text("Please provide a valid YouTube URL.")
        return

    await update.message.reply_text("Downloading audio...")

    output_path = "downloads/"
    os.makedirs(output_path, exist_ok=True)

    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio',
                               'outtmpl': f'{output_path}%(title)s.%(ext)s',
                               'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}) as ydl:
            ydl.download([url])

        audio_file = max(os.listdir(output_path), key=lambda x: os.path.getctime(os.path.join(output_path, x)))
        await update.message.reply_audio(audio=open(os.path.join(output_path, audio_file), 'rb'))
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("video", download_video))
    app.add_handler(CommandHandler("audio", download_audio))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
