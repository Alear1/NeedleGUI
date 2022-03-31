#GUI handler for NeedleGUI using tkinter

#To generate python file from .ui: pyuic5 -x test_ui_form.ui -o test.py


import weakref
import time
import test
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow:
    def __init__(self, parent):
        #Initialize all the required stuff for QT here

        self.parent = parent #This is the data handler object
            
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = test.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        self.ui.gpredict_btn.clicked.connect(self.gpredict_btn_clicked)
        self.ui.serial_btn.clicked.connect(self.serial_btn_clicked)
        self.ui.label_2.hide()

        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_gui_elements)
        self.update_timer.start(1000)

        sys.exit(self.app.exec_())
        #Examples:

    def update_gui_elements(self):
        #Updates all labels/values/etc every 1 second

        #Raw target update
        self.ui.raw_target_az.setText(str(self.parent.raw_target[0]))
        self.ui.raw_target_el.setText(str(self.parent.raw_target[1]))

    def gpredict_btn_clicked(self):
        #when gpredict button has been clicked:
        self.parent.start_gpredict_socket()
        self.ui.label_2.show()
    
    def serial_btn_clicked(self):
        self.parent.stop_gpredict_socket()
        self.ui.label_2.hide()

    def window_loop(self):
        #This is where the main loop of the window lives
        while True: #This should end up being while alive or sth like that
            self.update()
            position = self.parent.sercon.get_position()
            #Then send position to parent
            self.parent.sercon.send_data(b'S') #Arduino get state command
            state = self.parent.sercon.read_data() #Listen for the response for the arduino, then put the response string into state variable
            self.parse_state(state)

    def update(self):
        time.sleep(0.0001)
    
    def rotate_clockwise(self):
        try:
            if self.parent.serial_connection_enabled:
                #GREY OUT PARTS OF WINDOW DURING ROTATION
                self.parent.sercon.send_data(b'C1')
        except:
            print("ERROR: rotate command not sent")

    def parse_state(self, msg):
        #use space as delimiter to split string into individual sections
        #parse individual parts of string
        #send data to parent aka data handler
        #ideally scalable, takes a dict with position in string and corresponding variable
        pass

    #Start Gpredict Connection:
    #self.parent.start_gpredict_socket()
    #Stop Gpredict Connection:
    #self.parent.socket_connection_enabled = 0

    #Start Arduino Connection:
    #self.parent.serial_connection_enabled = 1
    #self.parent.serial_connection_enabled = 0