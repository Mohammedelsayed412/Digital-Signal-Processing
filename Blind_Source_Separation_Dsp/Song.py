# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Song.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Song(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.songOpen = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.songOpen.setFont(font)
        self.songOpen.setObjectName("songOpen")
        self.verticalLayout.addWidget(self.songOpen)
        self.widget_song = PlotWidget(self.centralwidget)
        self.widget_song.setObjectName("widget_song")
        self.verticalLayout.addWidget(self.widget_song)
        self.song_result = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.song_result.setFont(font)
        self.song_result.setObjectName("song_result")
        self.verticalLayout.addWidget(self.song_result)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionUpload_Song = QtWidgets.QAction(MainWindow)
        self.actionUpload_Song.setObjectName("actionUpload_Song")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Song Separation"))
        self.songOpen.setText(_translate("MainWindow", "Upload Song"))
        self.song_result.setText(_translate("MainWindow", "Show Results"))
        self.actionUpload_Song.setText(_translate("MainWindow", "Upload Song"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Song()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
