import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import whisper

import pytube as pt
from datetime import timedelta
import os
import moviepy.editor as mpy


@app.route('/')
def upload_form():
    return render_template('index.html')


ALLOWED_EXTENSIONS = ['mp4']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename == '':
        return 'No video selected'
    if video and allowed_file(video.filename):
        video.save('static/videos/' + video.filename)
        return render_template('preview.html', video_name=video.filename)
    return 'Invalid video file'


@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413


if __name__ == "__main__":
    app.run()
