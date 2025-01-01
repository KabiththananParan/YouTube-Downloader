import os
import re
from tqdm import tqdm
from pytubefix import Playlist, YouTube


def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '-', filename)

def download_playlist(url, resolution):
    playlist = Playlist(url)
    playlist_name = sanitize_filename(re.sub(r'\W+', '-', playlist.title))

    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
    
    for index, video in enumerate(tqdm(playlist.videos, desc="Downloading playlist", unit="video", start=1)):
        yt = YouTube(video.watch_url, on_progress_callback=progress_function)
        video_streams = yt.streams.filter(res=resolution)


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize



