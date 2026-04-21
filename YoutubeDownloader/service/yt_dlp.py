import yt_dlp 
import os
from django.conf import settings

def download_video(url):
    destination = os.path.join(settings.MEDIA_ROOT, 'videos')
    os.makedirs(destination, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': f'{destination}/%(title)s.%(ext)s', 
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return {
                'success': True,
                'title': info.get('title', 'Unknown Title'),
                'filename': ydl.prepare_filename(info),
                'path': f"videos/{info.get('title', 'Unknown Title')}.mp4"
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }