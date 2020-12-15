from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
from save import mainFolder

def Say(index,World):
    os.chdir(mainFolder)
    if (str(index)+".mp3") in os.listdir(".\Sounds"):
        playsound(f".\Sounds\{str(index)}.mp3")
    else:
        try:
            sound=gTTS(text=World,lang="en")
            os.chdir(mainFolder)
            sound.save(f".\Sounds\{str(index)}.mp3")
        except:
            os.remove(f".\Sounds\{str(index)}.mp3")
        else:
            playsound(f".\Sounds\{str(index)}.mp3")


def Record():
    r= sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice = r.recognize_google(audio,language="en-EN").lower()
            return(voice)
    except:
        return("I could not get")
        
        
