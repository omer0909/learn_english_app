import os
import json

mainFolder=os.getcwd()

try:
    os.mkdir("Sounds")
except:
    pass

os.chdir(os.getenv('APPDATA'))

try:
    os.mkdir("ozGames_learnEnglish")
except:
    pass
else:
    with open(os.getcwd()+"\ozGames_learnEnglish\save.json","w") as dosya:
        dosya.write(json.dumps([0]))



def Get(index):
    os.chdir(os.getenv('APPDATA')+"\ozGames_learnEnglish")
    with open(os.getcwd()+"\save.json","r") as dosya:
        value=json.loads(dosya.read())[index]
    return value

def Set(index,value):
    os.chdir(os.getenv('APPDATA')+"\ozGames_learnEnglish")
    with open(os.getcwd()+"\save.json","r") as dosya:
        old=json.loads(dosya.read())
    old[index]=value
    with open(os.getcwd()+"\save.json","w") as dosya:
        dosya.write(json.dumps(old))
