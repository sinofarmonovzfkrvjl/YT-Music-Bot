from youtubesearchpython import VideosSearch
import yt_dlp
from moviepy.editor import VideoFileClip
import os
import glob

def separate_audio_from_video(video_path, output_path="musiqa.mp3"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_path)

def Mp3Downloader(url: list) -> list:
    ydl_opts = {
        'outtmpl': "%(title)s.%(ext)s",
        'format': 'best[ext=mp4]',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    except Exception as e:
        print(e)
    # try:
    #     separate_audio_from_video(glob.glob("*.mp4")[0])
    # except Exception as e:
    #     print(e)
