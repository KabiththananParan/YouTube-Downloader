from pytubefix import Channel

c = Channel("url")
print(f"Downloading videos by: {c.channel_name}")

for video in c.videos:
    video.streams.get_highest_resolution().download()