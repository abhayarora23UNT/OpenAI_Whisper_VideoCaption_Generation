import whisper
from utils import *
from langdetect import detect, LangDetectException
import time

model=''

class GenerateCaptions:

    def __init__(self):
        self.loadWhisperModel()

    def loadWhisperModel(self):
        global model 
        model = whisper.load_model("base") # model can be changed to medium,large . Recompile Code #
        
        # offline load model #
        # model = whisper.load_model("C:/Users/Anubhav Arora/.cache/whisper/base.pt") # model can be changed to medium,large . Recompile Code #

    def generateCaptions(self,audioPath):
        resultObj ={}
        endUrl=audioPath.split("/")[-1]
        captionFileName=endUrl.rsplit('.', 1)[0].lower()
        downloadPath="static/captions/"+captionFileName+".txt"
        start_time = time.perf_counter()
        if model :
            result = model.transcribe(audioPath, fp16=False)
            # result = model.transcribe(audioPath, fp16=False, language='English')
            transcribeText = result["text"]
            try:
                detectedLang= detect(transcribeText)
            except LangDetectException as e:
                print("Error: Unable to detect Language ", e)
                detectedLang= 'en'

            print(transcribeText)
            print(detectedLang)

            with open(downloadPath, "w+",encoding="utf-8") as f:
                f.write(transcribeText)

            # captionFilePath=self.generateSrtFile(segments,captionFileName)
            captionFilePath=self.generateVttOutput(result,captionFileName)
            self.generateSrtOutput(result,captionFileName)
            resultObj[0] = captionFilePath
            resultObj[1]= detectedLang
            # For Debugging Purpose #
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.6f} seconds")
            #--------------------End-------------------#
            return resultObj

    def generateSrtOutput(self,result,audio):
        srt_writer = get_writer("srt", "static/videos/")
        srt_writer(result, audio)
        return audio+".srt"

    def generateVttOutput(self,result,audio):
        vtt_writer = get_writer("vtt", "static/videos/")
        vtt_writer(result, audio)
        return audio+".vtt"

    
 

