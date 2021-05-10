# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ECG.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ECG(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ecgopen = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ecgopen.setFont(font)
        self.ecgopen.setObjectName("ecgopen")
        self.verticalLayout.addWidget(self.ecgopen)
        self.widget_ecg = PlotWidget(self.centralwidget)
        self.widget_ecg.setObjectName("widget_ecg")
        self.verticalLayout.addWidget(self.widget_ecg)
        self.ecg_result = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ecg_result.setFont(font)
        self.ecg_result.setObjectName("ecg_result")
        self.verticalLayout.addWidget(self.ecg_result)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECG File Separation"))
        self.ecgopen.setText(_translate("MainWindow", "ECG File"))
        self.ecg_result.setText(_translate("MainWindow", "Show Results"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ECG()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
