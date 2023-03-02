import moviepy.editor as mpy

import pytube as pt
import os
import urllib.parse

class VideoConverter:

    def convertVideo2Audio(self,fileName):
        path=fileName.rsplit('.', 1)[0].lower()
        print(path)
        sourcePath="static/videos/"+fileName
        targetPath="static/audios/"+path
        clip = mpy.VideoFileClip(sourcePath)
      
        clip.audio.write_audiofile(targetPath+".wav")
        return targetPath+".wav"

    def downloadYTubeVideo(self,videoUrl):
        yt = pt.YouTube(videoUrl)
        stream = yt.streams.filter(only_audio=True)[0]
        print("Debug: ", stream)
        sourcePath ="static/videos/"
        # fileName = urllib.parse.quote(yt.title, safe="")+".mp4"
        fileName = "abc.mp4"
        stream.download(sourcePath, fileName)
        print(fileName)
        return fileName