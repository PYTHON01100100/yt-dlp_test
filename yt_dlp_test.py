from yt_dlp import YoutubeDL

URLS = ['https://youtu.be/JkBQw-Iik-o?feature=shared']

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',  # اسم الملف الناتج
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
