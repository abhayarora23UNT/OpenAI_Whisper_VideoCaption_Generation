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

from generatecaptions import GenerateCaptions
from video2audio import VideoConverter


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
        return doProcessing(video.filename)
    return 'Invalid video file'


def doProcessing(fileName):
    converter=VideoConverter()
    print("debug: File name is ",fileName)
    # youTube= "https://www.youtube.com/watch?v=dd1kN_myNDs"
    audioPath=converter.convertVideo2Audio(fileName)
    # videoPath= converter.downloadYTubeVideo(youTube);
    # audioPath = converter.convertVideo2Audio(videoPath)
    print("debug: audio path  is ",audioPath)
    return generateCaptions(fileName,audioPath)


def generateCaptions(videoFileName,audioPath):
    captionGen=GenerateCaptions()
    captionFilePath=captionGen.generateCaptions(audioPath)
    print("debug: caption path  is ",captionFilePath)
    return render_template('preview.html', video_name=videoFileName,captionFile=captionFilePath)


@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413


if __name__ == "__main__":
    app.run()
