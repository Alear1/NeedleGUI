#GUI handler for NeedleGUI using tkinter

#To generate python file from .ui: pyuic5 -x <form name> -o ui_form.py


import weakref
import time
import ui_form
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow:
    def __init__(self, parent):
        #Initialize all the required stuff for QT here

        self.parent = parent #This is the data handler object
            
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = ui_form.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
        #Serial and Socket connections
        self.ui.start_gpredict_btn.clicked.connect(self.start_gpredict)
        self.ui.stop_gpredict_btn.clicked.connect(self.stop_gpredict)
        self.ui.start_serial_btn.clicked.connect(self.start_serial)
        self.ui.stop_serial_btn.clicked.connect(self.stop_serial)
        self.ui.gpredict_connected_label.hide()
        self.ui.serial_connected_label.hide()

        #State connections
        self.ui.stop_btn.clicked.connect(self.emergency_stop)
        self.ui.stop_label.hide()

        #Timer for updating values every second
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_gui_elements)
        self.update_timer.start(1000)

        sys.exit(self.app.exec_())
        #Examples:

    def update_gui_elements(self):
        #Updates all labels/values/etc every 1 second

        #raw target update
        self.ui.raw_target_az.setText(str(self.parent.raw_target[0]))
        self.ui.raw_target_el.setText(str(self.parent.raw_target[1]))

        #now we want to update the position and the states from the serial by adding get pos command
        #and get state command to the serial_msg_queue
        self.parent.serial_msg_queue.append("p")
        self.parent.serial_msg_queue.append("S")
        self.ui.raw_pos_az.setText(str(self.parent.raw_position[0]))
        self.ui.raw_pos_el.setText(str(self.parent.raw_position[1]))

        #send current target to Arduino if target set command sent from gpredict:
        if self.parent.new_target:
            self.parent.new_target = 0
            self.parent.serial_msg_queue.append("P " + str(self.parent.current_target[0]) + " " + str(self.parent.current_target[1]))
        
    def start_gpredict(self):
        #when gpredict button has been clicked:
        self.parent.start_gpredict_socket()
        self.ui.gpredict_connected_label.show()

    def stop_gpredict(self):
        self.parent.stop_gpredict_socket()
        self.ui.gpredict_connected_label.hide()
    
    def start_serial(self):
        self.parent.start_serial_connection()
        self.ui.serial_connected_label.show()
    
    def stop_serial(self):
        self.parent.stop_serial_connection()
        self.ui.serial_connected_label.hide()

    def emergency_stop(self):
        if self.parent.state_variables["Emergency Stop"]:   #if system is already in stopped state
            self.parent.serial_msg_queue.append("E0")       #send unstop message
            self.ui.stop_label.hide()                                       #hide label
        else:               
            self.parent.serial_msg_queue.append("E1")       #send stop message
            self.ui.stop_label.show()                                      #show label


    def window_loop(self):
        #This is where the main loop of the window lives
        while True:
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
