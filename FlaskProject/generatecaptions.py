import whisper
from utils import *


model=''

class GenerateCaptions:

    def __init__(self):
        self.loadWhisperModel()

    def loadWhisperModel(self):
        global model 
        model = whisper.load_model("base") # model can be changed to medium,large . Recompile Code #

    def generateCaptions(self,audioPath):
        endUrl=audioPath.split("/")[-1]
        captionFileName=endUrl.rsplit('.', 1)[0].lower()
        downloadPath="static/captions/"+captionFileName+".txt"
        if model :
            # result = model.transcribe(audioPath, fp16=False)
            result = model.transcribe(audioPath, fp16=False, language='English')
            print(result["text"])
            with open(downloadPath, "w+",encoding="utf-8") as f:
                f.write(result["text"])

            # captionFilePath=self.generateSrtFile(segments,captionFileName)
            captionFilePath=self.generateVttOutput(result,captionFileName)
            self.generateSrtOutput(result,captionFileName)
            return captionFilePath

    def generateSrtOutput(self,result,audio):
        srt_writer = get_writer("srt", "static/videos/")
        srt_writer(result, audio)
        return audio+".srt"

    def generateVttOutput(self,result,audio):
        vtt_writer = get_writer("vtt", "static/videos/")
        vtt_writer(result, audio)
        return audio+".vtt"

    
 

