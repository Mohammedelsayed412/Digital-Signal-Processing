# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'party.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_party(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 578)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 1101, 554))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.party1 = QtWidgets.QPushButton(self.widget)
        self.party1.setObjectName("party1")
        self.verticalLayout.addWidget(self.party1)
        self.party2 = QtWidgets.QPushButton(self.widget)
        self.party2.setObjectName("party2")
        self.verticalLayout.addWidget(self.party2)
        self.result_party = QtWidgets.QPushButton(self.widget)
        self.result_party.setObjectName("result_party")
        self.verticalLayout.addWidget(self.result_party)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(138, 428, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.widget_party = PlotWidget(self.widget)
        self.widget_party.setObjectName("widget_party")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widget_party)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cocktail party"))
        self.party1.setText(_translate("MainWindow", "Cocktail One"))
        self.party2.setText(_translate("MainWindow", "Cocktail Two"))
        self.result_party.setText(_translate("MainWindow", "Show Results"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_party()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
