import moviepy.editor as mpy

import pytube as pt

class VideoConverter:

    def convertVideo2Audio(self,fileName):
        path=fileName.rsplit('.', 1)[0].lower()
        print(path)
        sourcePath="static/videos/"+fileName
        targetPath="static/audios/"+path
        clip = mpy.VideoFileClip(sourcePath)
      
        clip.audio.write_audiofile(targetPath+".wav")
        return targetPath+".wav"

    def convertYTubeVideo2Audio(self,videoUrl,fileName):
        yt = pt.YouTube(videoUrl)
        stream = yt.streams.filter(only_audio=True)[0]
        sourcePath="static/videos/"+fileName
        stream.download(sourcePath)
        return sourcePath