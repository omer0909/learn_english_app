from PySide2 import QtWidgets,QtCore
from gtts import gTTS
import os
from save import mainFolder
from worlds import *
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
                    World=""
                    if self.index <200:
                        World=worldsEn1[self.index]
                    elif self.index <400:
                        World=worldsEn2[self.index%200]
                    elif self.index <600:
                        World=worldsEn3[self.index%200]
                    elif self.index <800:
                        World=worldsEn4[self.index%200]
                    else:
                        World=worldsEn5[self.index%200]
                    try:
                        sound=gTTS(text=World,lang="en")
                        os.chdir(mainFolder)
                        sound.save(f".\Sounds\{str(self.index)}.mp3")
                    except:
                        time.sleep(0.1)
                        self.change_value.emit(-1)
                    else:
                        self.change_value.emit(len(files))

                    if not Path(f".\Sounds\{str(self.index)}.mp3").stat().st_size < 1:
                        self.index+=1
                    else:
                        os.chdir(mainFolder)
                        os.remove(f".\Sounds\{str(self.index)}.mp3")
                else:
                    self.index+=1
            else:
                self.change_value.emit(1000)
                self.active=False
                