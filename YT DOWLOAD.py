# 📦 Install yt-dlp
!pip install -q yt-dlp

# 📁 Imports
import os
import shutil
from IPython.display import FileLink

# 🔗 Ask for playlist
playlist_url = input("🔗 Enter the YouTube playlist URL: ").strip()

# 🎧 Format choice
print("\n🎧 What format do you want to download?")
print("1. Audio Only (MP3)")
print("2. Full Video (MP4)")
choice = input("Enter 1 or 2: ").strip()

# 📂 Setup folder
download_dir = "yt_downloads"
os.makedirs(download_dir, exist_ok=True)

# 🎯 Build yt-dlp command
if choice == '1':
    ytdlp_command = f'yt-dlp -f "bestaudio" --extract-audio --audio-format mp3 -o "{download_dir}/%(playlist_index)s - %(title).100s.%(ext)s" "{playlist_url}"'
    print("\n🎧 Downloading as MP3 (audio only)...")

elif choice == '2':
    # 🧠 Ask for resolution
    print("\n📺 Choose your preferred resolution:")
    print("1. 360p")
    print("2. 480p")
    print("3. 720p")
    print("4. 1080p")
    print("5. Best available")
    res_choice = input("Enter 1–5: ").strip()

    res_map = {
        '1': '360',
        '2': '480',
        '3': '720',
        '4': '1080',
        '5': None  # best
    }

    selected_res = res_map.get(res_choice, None)

    if selected_res:
        ytdlp_format = f'bestvideo[ext=mp4][height<={selected_res}]+bestaudio[ext=m4a]/best[ext=mp4][height<={selected_res}]'
        print(f"\n🎥 Downloading video in ≤{selected_res}p resolution (MP4)...")
    else:
        ytdlp_format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
        print("\n🎥 Downloading best available quality (MP4)...")

    ytdlp_command = f'yt-dlp -f "{ytdlp_format}" -o "{download_dir}/%(playlist_index)s - %(title).100s.%(ext)s" "{playlist_url}"'

else:
    print("❌ Invalid choice. Please enter 1 or 2.")
    raise SystemExit

# 🚀 Run download
!{ytdlp_command}

# 🗜️ Zip the downloaded folder
shutil.make_archive("lectures_download", 'zip', download_dir)
print("\n✅ Zipped the content into: lectures_download.zip")

# 📥 Provide download link
display(FileLink("lectures_download.zip"))
