from youtubesearchpython import VideosSearch
import yt_dlp

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
