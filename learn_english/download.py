from PySide2 import QtWidgets,QtCore
from gtts import gTTS
import os
from save import mainFolder
from words import *
from downloadUi import*
import time
from pathlib import Path


class dClass(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Download_Form()
        self.ui.setupUi(self)
        self.isthread=downloadTread()
        self.isthread.change_value.connect(self.setvalue)
        
    def dStart(self):
        self.isthread.active=True
        self.isthread.start()

    def closeEvent(self,event):
        self.isthread.active=False
    
    def setvalue(self,val):
        if val<0:
            self.ui.label.setText(str("No connection"))
            self.ui.pushButton.setText("Cancel")
        else:
            self.ui.progressBar.setValue(val)
            if val==1000:
                self.ui.label.setText(str(f"Completed"))
                self.ui.pushButton.setText("OK")
            else:
                self.ui.label.setText(str(f"Downloading...  {val}/1000"))
                self.ui.pushButton.setText("Cancel")
    
class downloadTread(QtCore.QThread):

    change_value=QtCore.Signal(int)
    active=False
    index=0


    def stop(self):
        self.active=False
    def run(self):
        self.index=0

        os.chdir(mainFolder)
        self.change_value.emit(len(os.listdir(".\Sounds")))
        
        while self.active:
            os.chdir(mainFolder)
            files=os.listdir(".\Sounds")
            if 1000 > len(files):
                if not (str(self.index)+".mp3") in files:
                    Word=""
                    if self.index <200:
                        Word=wordsEn1[self.index]
                    elif self.index <400:
                        Word=wordsEn2[self.index%200]
                    elif self.index <600:
                        Word=wordsEn3[self.index%200]
                    elif self.index <800:
                        Word=wordsEn4[self.index%200]
                    else:
                        Word=wordsEn5[self.index%200]
                    try:
                        sound=gTTS(text=Word,lang="en")
                        os.chdir(mainFolder)
                        sound.save(f".\Sounds\{str(self.index)}.mp3")
                    except:
                        self.change_value.emit(-1)
                        os.chdir(mainFolder)
                        os.remove(f".\Sounds\{str(self.index)}.mp3")
                        time.sleep(0.1)
                    else:
                        self.change_value.emit(len(files))
                        self.index+=1
                else:
                    self.index+=1
            else:
                self.change_value.emit(1000)
                self.active=False
                
