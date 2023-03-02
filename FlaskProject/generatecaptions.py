import whisper
from datetime import timedelta
import os


model=''

class GenerateCaptions:

    def __init__(self):
        self.loadWhisperModel()

    def loadWhisperModel(self):
        global model 
        model = whisper.load_model("base")

    def generateCaptions(self,audioPath):
        endUrl=audioPath.split("/")[-1]
        captionFileName=endUrl.rsplit('.', 1)[0].lower()
        downloadPath="static/captions/"+captionFileName+".txt"
        if model :
            result = model.transcribe(audioPath, fp16=False, language='English')
            print(result["text"])
            with open(downloadPath, "w+") as f:
                f.write(result["text"])

            segments = result['segments']
            captionFilePath=self.generateSrtFile(segments,captionFileName)
            return captionFilePath

    def generateSrtFile(self,segments,fileName):
        for segment in segments:
            startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
            endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
            text = segment['text']
            segmentId = segment['id']+1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

            srtFilename = os.path.join("static/captions/", f""+fileName+".srt")

            with open(srtFilename, 'a', encoding='utf-8') as srtFile:
                srtFile.write(segment)

            print("debug: ",srtFilename)
            return srtFilename