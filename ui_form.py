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
        MainWindow.resize(649, 465)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_gpredict_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_gpredict_btn.setGeometry(QtCore.QRect(50, 70, 251, 40))
        self.start_gpredict_btn.setObjectName("start_gpredict_btn")
        self.start_serial_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_serial_btn.setGeometry(QtCore.QRect(310, 70, 281, 40))
        self.start_serial_btn.setObjectName("start_serial_btn")
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(250, 10, 131, 31))
        self.Title_Label.setScaledContents(False)
        self.Title_Label.setObjectName("Title_Label")
        self.gpredict_connected_label = QtWidgets.QLabel(self.centralwidget)
        self.gpredict_connected_label.setGeometry(QtCore.QRect(130, 40, 91, 24))
        self.gpredict_connected_label.setObjectName("gpredict_connected_label")
        self.serial_connected_label = QtWidgets.QLabel(self.centralwidget)
        self.serial_connected_label.setGeometry(QtCore.QRect(400, 40, 101, 24))
        self.serial_connected_label.setObjectName("serial_connected_label")
        self.raw_target_az = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_target_az.setGeometry(QtCore.QRect(50, 190, 113, 38))
        self.raw_target_az.setReadOnly(True)
        self.raw_target_az.setObjectName("raw_target_az")
        self.raw_target_el = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_target_el.setGeometry(QtCore.QRect(170, 190, 113, 38))
        self.raw_target_el.setReadOnly(True)
        self.raw_target_el.setObjectName("raw_target_el")
        self.stop_gpredict_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_gpredict_btn.setGeometry(QtCore.QRect(50, 110, 251, 40))
        self.stop_gpredict_btn.setObjectName("stop_gpredict_btn")
        self.stop_serial_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_serial_btn.setGeometry(QtCore.QRect(310, 110, 281, 40))
        self.stop_serial_btn.setObjectName("stop_serial_btn")
        self.raw_tgt_label = QtWidgets.QLabel(self.centralwidget)
        self.raw_tgt_label.setGeometry(QtCore.QRect(120, 160, 131, 24))
        self.raw_tgt_label.setObjectName("raw_tgt_label")
        self.raw_pos_label = QtWidgets.QLabel(self.centralwidget)
        self.raw_pos_label.setGeometry(QtCore.QRect(390, 160, 111, 24))
        self.raw_pos_label.setObjectName("raw_pos_label")
        self.raw_pos_az = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_pos_az.setGeometry(QtCore.QRect(330, 190, 113, 38))
        self.raw_pos_az.setReadOnly(True)
        self.raw_pos_az.setObjectName("raw_pos_az")
        self.raw_pos_el = QtWidgets.QLineEdit(self.centralwidget)
        self.raw_pos_el.setGeometry(QtCore.QRect(450, 190, 113, 38))
        self.raw_pos_el.setReadOnly(True)
        self.raw_pos_el.setObjectName("raw_pos_el")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(50, 240, 231, 51))
        self.stop_btn.setDefault(False)
        self.stop_btn.setFlat(False)
        self.stop_btn.setObjectName("stop_btn")
        self.stop_label = QtWidgets.QLabel(self.centralwidget)
        self.stop_label.setGeometry(QtCore.QRect(130, 280, 91, 51))
        self.stop_label.setObjectName("stop_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEST gui"))
        self.start_gpredict_btn.setText(_translate("MainWindow", "Start Gpredict Connection"))
        self.start_serial_btn.setText(_translate("MainWindow", "Start Serial Connection"))
        self.Title_Label.setText(_translate("MainWindow", "NEEDLEGUI V1"))
        self.gpredict_connected_label.setText(_translate("MainWindow", "Connected"))
        self.serial_connected_label.setText(_translate("MainWindow", "Connected"))
        self.stop_gpredict_btn.setText(_translate("MainWindow", "Stop Gpredict Connection"))
        self.stop_serial_btn.setText(_translate("MainWindow", "Stop Serial Connection"))
        self.raw_tgt_label.setText(_translate("MainWindow", "Raw Target"))
        self.raw_pos_label.setText(_translate("MainWindow", "Raw Position"))
        self.stop_btn.setText(_translate("MainWindow", "EMERGENCY STOP"))
        self.stop_label.setText(_translate("MainWindow", "STOPPED"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
