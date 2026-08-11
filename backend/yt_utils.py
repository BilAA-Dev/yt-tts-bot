import re
import requests
from yt_dlp import YoutubeDL

def get_channel_id_from_username(username):
    url = f"https://www.youtube.com/@{username}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return None
        match = re.search(r'"channelId":"([^"]+)"', r.text)
        return match.group(1) if match else None
    except:
        return None

def get_live_video_id(channel_id):
    ydl_opts = {'quiet': True, 'extract_flat': True, 'skip_download': True}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/channel/{channel_id}/live", download=False)
            return info.get('id')
    except:
        return None

def get_live_chat_id(video_id):
    ydl_opts = {'quiet': True, 'extract_flat': True, 'skip_download': True}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            return info.get('live_chat_id')
    except:
        return None