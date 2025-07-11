# 📦 Install yt-dlp
!pip install -q yt-dlp

# 📁 Imports
import os
import shutil
from IPython.display import FileLink

# 🧾 Ask user for input
playlist_url = input("🔗 Enter the YouTube playlist URL: ").strip()

print("\n🎧 What format do you want to download?")
print("1. Audio Only (MP3)")
print("2. Full Video (MP4)")
choice = input("Enter 1 or 2: ").strip()

# 📂 Setup download directory
download_dir = "yt_downloads"
os.makedirs(download_dir, exist_ok=True)

# 🎯 Build yt-dlp command
if choice == '1':
    ytdlp_command = f'yt-dlp -f "bestaudio" --extract-audio --audio-format mp3 -o "{download_dir}/%(playlist_index)s - %(title).100s.%(ext)s" "{playlist_url}"'
    print("\n🎧 Downloading as MP3 (audio only)...")
elif choice == '2':
    ytdlp_command = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4][height<=720]" -o "{download_dir}/%(playlist_index)s - %(title).100s.%(ext)s" "{playlist_url}"'
    print("\n🎥 Downloading as MP4 (video)...")
else:
    print("❌ Invalid choice. Please enter 1 or 2.")
    raise SystemExit

# 🚀 Run download
!{ytdlp_command}

# 🗜️ Zip the downloaded folder
shutil.make_archive("lectures_download", 'zip', download_dir)
print("\n✅ Zipped the videos into: lectures_download.zip")

# 📥 Provide download link
display(FileLink("lectures_download.zip"))
