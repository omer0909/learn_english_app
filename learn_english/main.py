import sys
from PySide2.QtWidgets import *
import random
import save
from words import *
from window import Ui_Form
import sound
import download


import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)



class SceneClass():
    def __init__(self,ui):
        self.uiClass=ui
        self.ui=ui.ui
        self.level=self.ui.comboBox.currentIndex()
        self.mixer(self.ui.spinBox.value())
        self.wordIndex=0
        self.ui.lineEdit.returnPressed.connect(self.control)
        self.selectTuple()
        self.viewer()
        self.ui.pushButton_6.clicked.connect(self.answer)
        self.ui.pushButton_4.clicked.connect(self.record)
        self.ui.pushButton_5.clicked.connect(self.wordSound)
        self.ui.lineEdit.setText("")
        self.getBool=False
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox.clicked.connect(self.checkBoxBool)


    def checkBoxBool(self,value):
        self.getBool=value

    def wordSound(self):
        sound.Say(self.words[self.wordIndex]+self.level*200,self.english[self.words[self.wordIndex]])

    def record(self):
        self.ui.lineEdit.setText(sound.Record())


    def answer(self):
        message=QMessageBox()
        message.setWindowTitle("Answer")
        message.setText(self.english[self.words[self.worldIndex]])
        message.exec_()

    def selectTuple(self):
        if self.level==0:
            self.turkish=wordsTr1
            self.english=wordsEn1
        if self.level==1:
            self.turkish=wordsTr2
            self.english=wordsEn2
        if self.level==2:
            self.turkish=wordsTr3
            self.english=wordsEn3
        if self.level==3:
            self.turkish=wordsTr4
            self.english=wordsEn4
        if self.level==4:
            self.turkish=wordsTr5
            self.english=wordsEn5

    def viewer(self):
        self.ui.soru.setText(self.turkish[self.words[self.wordIndex]])
        record=save.Get(0)
        if((self.level+1)*200<=record):
            value=200
        else:
            value=record%200
        self.ui.label_2.setText(str(self.wordIndex+1)+"/"+ str(value))

    def control(self):
        if self.english[self.words[self.wordIndex]].strip().lower()==self.ui.lineEdit.text().strip().lower():
            self.scoreTable()

        self.ui.lineEdit.setText("")

    def mixer(self,mix):
        self.words=list(range(mix))
        random.shuffle(self.words)
        self.words=self.words+list(range(mix,200))

    def scoreTable(self):
        if self.getBool:
            self.wordSound()

        self.wordIndex+=1
        record=save.Get(0)
        if record < self.wordIndex+(self.level*200):
            record+=1
            save.Set(0,record)
            
        if(self.wordIndex==200):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.label_4.setText("Record: "+ str(save.Get(0)))
            self.uiClass.levelEditor()
        else:
            self.viewer()

class appClass(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.goScene)
        self.ui.pushButton_3.clicked.connect(self.goMenu)
        self.ui.pushButton.clicked.connect(self.download)
        self.ui.label_4.setText("Record: "+ str(save.Get(0)))
        self.levelEditor()
        self.dMessage=download.dClass()
        
        
    def levelEditor(self):
        record=save.Get(0)
        if 200<=record and self.ui.comboBox.count()<=1:
            self.ui.comboBox.addItem("200-400")
        if 400<=record and self.ui.comboBox.count()<=2:
            self.ui.comboBox.addItem("400-600")
        if 600<=record and self.ui.comboBox.count()<=3:
            self.ui.comboBox.addItem("600-800")
        if 800<=record and self.ui.comboBox.count()<=4:
            self.ui.comboBox.addItem("800-1000")

    def goMenu(self):
        message=QMessageBox.question(self,"Close Application","Are you sure?",QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Cancel)
        if QMessageBox.Ok==message:
            self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.label_4.setText("Record: "+ str(save.Get(0)))
        self.levelEditor()

    def goScene(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.scene=SceneClass(self)
    
    def download(self):
        self.dMessage.show()
        self.dMessage.dStart()

    def closeEvent(self,event):
        if self.ui.stackedWidget.currentIndex()==1:
            message=QMessageBox.question(self,"Close Application","Are you sure?",QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Cancel)
            if QMessageBox.Ok==message:
                event.accept()
            else:
                event.ignore()

application=QApplication([])
application.setStyle("Fusion")
app=appClass()
app.show()
application.exec_()
