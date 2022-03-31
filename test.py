# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 287)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gpredict_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gpredict_btn.setGeometry(QtCore.QRect(50, 70, 251, 40))
        self.gpredict_btn.setObjectName("gpredict_btn")
        self.serial_btn = QtWidgets.QPushButton(self.centralwidget)
        self.serial_btn.setGeometry(QtCore.QRect(310, 70, 281, 40))
        self.serial_btn.setObjectName("serial_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 211, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 101, 24))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 110, 101, 24))
        self.label_3.setObjectName("label_3")
        self.raw_target_az = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_target_az.setGeometry(QtCore.QRect(30, 150, 113, 38))
        self.raw_target_az.setReadOnly(True)
        self.raw_target_az.setObjectName("raw_target_az")
        self.raw_target_el = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_target_el.setGeometry(QtCore.QRect(180, 150, 113, 38))
        self.raw_target_el.setReadOnly(True)
        self.raw_target_el.setObjectName("raw_target_el")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEST gui"))
        self.gpredict_btn.setText(_translate("MainWindow", "Start Gpredict Connection"))
        self.serial_btn.setText(_translate("MainWindow", "Start Serial Connection"))
        self.label.setText(_translate("MainWindow", "TEST GUI FOR NEEDLEGUI"))
        self.label_2.setText(_translate("MainWindow", "Connected"))
        self.label_3.setText(_translate("MainWindow", "Connected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
