# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(556, 458)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.gridLayout = QGridLayout(self.menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 30pt \"Impact\";\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.menu)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.menu)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.menu)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(200)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSlider = QSlider(self.menu)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(200, 0))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.comboBox = QComboBox(self.menu)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.menu)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 1, 1)

        self.line = QFrame(self.menu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.menu)
        self.scene = QWidget()
        self.scene.setObjectName(u"scene")
        self.gridLayout_2 = QGridLayout(self.scene)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.soru = QLabel(self.scene)
        self.soru.setObjectName(u"soru")
        self.soru.setScaledContents(False)
        self.soru.setAlignment(Qt.AlignCenter)
        self.soru.setWordWrap(True)

        self.gridLayout_2.addWidget(self.soru, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_5 = QPushButton(self.scene)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.checkBox = QCheckBox(self.scene)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.lineEdit = QLineEdit(self.scene)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_4 = QPushButton(self.scene)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.scene)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.scene)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.scene)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.scene)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 1, 1, 1)


        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.horizontalSlider.setValue)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Learn English", None))
        self.label.setText(QCoreApplication.translate("Form", u"LEARN ENGL\u0130SH", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Record:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Mix", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Play Level", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"0-200", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"Download Sounds", None))
        self.soru.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"sound", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"auto", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"michrophone", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"menu", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"answer", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"00/00", None))
    # retranslateUi

