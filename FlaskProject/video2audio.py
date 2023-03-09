import moviepy.editor as mpy

import pytube as pt
import os
import urllib.parse
from pytube import extract

class VideoConverter:

    def convertVideo2Audio(self,fileName):
        path=fileName.rsplit('.', 1)[0].lower()
        print(path)
        sourcePath="static/videos/"+fileName
        targetPath="static/audios/"+path
        clip = mpy.VideoFileClip(sourcePath)
        print("Debug: ",targetPath)
        clip.audio.write_audiofile(targetPath+".wav")
        return targetPath+".wav"

    def downloadYTubeVideo(self,videoUrl):
        yt = pt.YouTube(videoUrl)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print("Debug: ", stream)
        sourcePath ="static/videos/"
        videoId=extract.video_id(videoUrl)
        fileName = urllib.parse.quote(videoId, safe="")+".mp4"
        stream.download(sourcePath, fileName)
        print(fileName)
        return fileName