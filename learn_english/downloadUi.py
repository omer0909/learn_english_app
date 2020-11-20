# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloadUi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Download_Form(object):
    def setupUi(self, Download_Form):
        if not Download_Form.objectName():
            Download_Form.setObjectName(u"Download_Form")
        Download_Form.resize(251, 89)
        self.verticalLayout = QVBoxLayout(Download_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Download_Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(1000)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.label = QLabel(Download_Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Download_Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Download_Form)
        self.pushButton.clicked.connect(Download_Form.close)

        QMetaObject.connectSlotsByName(Download_Form)
    # setupUi

    def retranslateUi(self, Download_Form):
        Download_Form.setWindowTitle(QCoreApplication.translate("Download_Form", u"Download", None))
        self.label.setText(QCoreApplication.translate("Download_Form", u"Downloading...  0/1000", None))
        self.pushButton.setText(QCoreApplication.translate("Download_Form", u"Cancel", None))
    # retranslateUi

