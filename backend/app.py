from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from gtts import gTTS
import os
import time
import json
import requests
from yt_utils import *

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../frontend', path)

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({'status': 'error', 'message': 'Username kosong!'})
    
    channel_id = get_channel_id_from_username(username)
    if not channel_id:
        return jsonify({'status': 'error', 'message': 'Username gak ditemukan!'})
    
    video_id = get_live_video_id(channel_id)
    if not video_id:
        return jsonify({'status': 'error', 'message': 'Channel gak live!'})
    
    chat_id = get_live_chat_id(video_id)
    if not chat_id:
        return jsonify({'status': 'error', 'message': 'Gagal dapetin chat ID!'})
    
    return jsonify({'status': 'ok', 'chat_id': chat_id, 'video_id': video_id})

@app.route('/tts', methods=['POST'])
def tts_manual():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'gak ada teks'}), 400
    tts = gTTS(text=text, lang='id')
    filename = f"tts_{int(time.time())}.mp3"
    tts.save(filename)
    return send_file(filename, as_attachment=False)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
