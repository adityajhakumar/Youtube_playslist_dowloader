from pytube import Playlist
import os
import time

def download_video(video, output_path):
    print(f"Downloading: {video.title}")
    success = False
    for attempt in range(3):  # Retry up to 3 times
        try:
            video.streams.first().download(output_path, timeout=10)
            print(f"{video.title} downloaded successfully!")
            success = True
            break  # Exit retry loop if download succeeds
        except Exception as e:
            print(f"Error downloading {video.title}: {e}")
            print(f"Retrying download: {video.title}")
            time.sleep(5)  # Wait for 5 seconds before retrying
    if not success:
        print(f"Failed to download {video.title}")

def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url)
    print(f"Downloading {len(playlist)} videos from the playlist: {playlist.title}...")

    for index, video in enumerate(playlist.videos, start=1):
        print(f"Video {index}/{len(playlist)}")
        download_video(video, output_path)

if __name__ == "__main__":
    playlist_url = input("Enter the url of playlist: ")
    output_path = input("Enter the output directory path: ").strip('"')  # Strip quotes from the input
    os.makedirs(output_path, exist_ok=True)  # Ensure the directory exists or create it
    download_playlist(playlist_url, output_path)
