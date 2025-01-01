from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
import os

url = "https://www.youtube.com/watch?v=SbAKYgfYET8&pp=ygUFbXVzaWM%3D"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Download audio as .m4a
ys = yt.streams.get_audio_only()
download_path = ys.download()

# Convert the downloaded .m4a to .mp3
m4a_audio = AudioSegment.from_file(download_path, format="m4a")
mp3_path = download_path.replace(".m4a", ".mp3")
m4a_audio.export(mp3_path, format="mp3")

# Delete the original .m4a file
os.remove(download_path)

print(f"Downloaded and converted to {mp3_path}")