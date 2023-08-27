#To generate python file from .ui: pyuic5 -x NeedleGUI_ui_form_v1.ui -o ui_form.py

import weakref
import time

from pip import main
import ui_form
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from numpy import linspace, cos, sin, pi
import data_handler

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
        self.ui.gpredict_connect_btn.clicked.connect(self.gpredict_button)
        self.ui.serial_connect_btn.clicked.connect(self.serial_button)
        self.ui.gpredict_port_input.setText(str(self.parent.socket_addr))
        self.ui.serial_port_input.setText(self.parent.serial_port_addr)
        self.ui.gpredict_port_input.textChanged.connect(self.gpredict_port_update) 
        self.ui.serial_port_input.textChanged.connect(self.serial_port_update)

        #Raw target reset button:
        self.ui.raw_tgt_reset_btn.clicked.connect(self.raw_target_reset)

        #Spiral search
        # self.ui.resolution_spinBox.setText(str(self.parent.ss_resolution))
        self.ui.resolution_spinBox.textChanged.connect(self.spiral_search_update)
        self.ui.angular_spacing_spinBox.textChanged.connect(self.spiral_search_update)
        self.ui.search_button.clicked.connect(self.spiral_search_button)

        #manual offset:
        self.ui.manual_offset_el_minus.hide()
        self.ui.manual_offset_az_minus.hide()
        self.ui.az_offset_hundredup_btn.clicked.connect(self.man_bt_1)
        self.ui.az_offset_tenup_btn.clicked.connect(self.man_bt_2)
        self.ui.az_offset_oneup_btn.clicked.connect(self.man_bt_3)
        self.ui.az_offset_tenthup_btn.clicked.connect(self.man_bt_4)
        self.ui.az_offset_hundreddn_btn.clicked.connect(self.man_bt_5)
        self.ui.az_offset_tendn_btn.clicked.connect(self.man_bt_6)
        self.ui.az_offset_onedn_btn.clicked.connect(self.man_bt_7)
        self.ui.az_offset_tenthdn_btn.clicked.connect(self.man_bt_8)

        self.ui.el_offset_tenup_btn.clicked.connect(self.man_bt_9)
        self.ui.el_offset_oneup_btn.clicked.connect(self.man_bt_10)
        self.ui.el_offset_tenthup_btn.clicked.connect(self.man_bt_11)
        self.ui.el_offset_tendn_btn.clicked.connect(self.man_bt_12)
        self.ui.el_offset_onedn_btn.clicked.connect(self.man_bt_13)
        self.ui.el_offset_tenthdn_btn.clicked.connect(self.man_bt_14)

        #Tharusha Unwind CCW and Unwind CW 2023-07-01
        self.ui.unwind_ccw_btn.pressed.connect(self.unwind_ccw)
        self.ui.unwind_ccw_btn.released.connect(self.unwind_stop)
        self.ui.unwind_cw_btn.pressed.connect(self.unwind_cw)
        self.ui.unwind_cw_btn.released.connect(self.unwind_stop)

        #auto offset:
        self.ui.auto_offset_az_minus.hide()
        self.ui.auto_offset_el_minus.hide()

        #State connections
        #self.ui.stop_btn.clicked.connect(self.emergency_stop)
        #self.ui.stop_label.hide()

        self.update_gui_elements()
        #Timer for updating values every second
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_gui_elements)
        self.update_timer.start(1)

        sys.exit(self.app.exec_())
        #Examples:

    def update_gui_elements(self):
        #Updates all labels/values/etc every 1 second

        #Spiral search coords update
        self.coords = self.parent.coords

        #raw target update
        if self.parent.gpredict_connection:
            self.ui.raw_tgt_az_label.setText("{:05.1f}".format(self.parent.raw_target[0]))
            self.ui.raw_tgt_el_label.setText("{:04.1f}".format(self.parent.raw_target[1]))

        #Update raw position from serial, update position and state variables
        if self.parent.serial_connection and ("AZ EL" not in self.parent.serial_msg_queue):
            self.parent.serial_msg_queue.append("AZ EL")
            #self.parent.serial_msg_queue.append("S")
            self.ui.raw_pos_az_label.setText("{:05.1f}".format(self.parent.raw_position[0]))
            self.ui.raw_pos_el_label.setText("{:04.1f}".format(self.parent.raw_position[1]))
        
        if not self.parent.serial_connection:
            self.ui.serial_connect_btn.setText("Open Serial Connection")
            self.ui.serial_state_str.setText("Disconnected")
        elif self.parent.serial_connection:
            self.ui.serial_connect_btn.setText("Close Serial Connection")
            self.ui.serial_state_str.setText("Connected")

        #update serial and socket connection state:
        if self.parent.socket_connection_enabled and not self.parent.gpredict_connection:
            self.ui.gpredict_connect_btn.setDisabled(True)
            self.ui.gpredict_state_str.setText("Connecting...")
        elif self.parent.gpredict_connection:
            self.ui.gpredict_connect_btn.setDisabled(False)
            self.ui.gpredict_connect_btn.setText("Close Gpredict Connection")
            self.ui.gpredict_state_str.setText("Connected")
        else:
            self.ui.gpredict_connect_btn.setDisabled(False)
            self.ui.gpredict_connect_btn.setText("Open Gpredict Connection")
            self.ui.gpredict_state_str.setText("Disconnected")

        #Update Current target:
        self.parent.update_current_target()
        self.ui.sent_tgt_az_label.setText("{:05.1f}".format(self.parent.current_target[0]))
        self.ui.sent_tgt_el_label.setText("{:04.1f}".format(self.parent.current_target[1]))

        #send current target to Arduino if target set command sent from gpredict:
        if self.parent.new_target and self.parent.serial_connection:
            self.parent.new_target = 0
            print('self.parent.current_target = ', self.parent.current_target)
            # self.parent.serial_msg_queue.append("P " + str(self.parent.current_target[0]) + " " + str(self.parent.current_target[1]))
            self.parent.serial_msg_queue.append("AZ" + str(self.parent.current_target[0]) + " EL" + str(self.parent.current_target[1]))
        
    def spiral_search_button(self):
        if self.parent.spiral_search_connection:
            self.stop_spiral_search()
        else:
            self.start_spiral_search()
    
    def start_spiral_search(self):
        self.ui.search_button.setText('Stop Search')
        print('starting spiral search')
        print('angular spacing:', self.parent.ss_angular_spacing, '|| resolution:', self.parent.ss_resolution)
        self.parent.spiral_search_connection = 1
        self.thread = QThread()
        self.worker = ss_Worker(self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def stop_spiral_search(self):
        self.ui.search_button.setText('Start Search')
        self.parent.spiral_search_connection = 0
        print('stopping spiral search')
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()

    def spiral_search_update(self):
        self.parent.ss_resolution = int(self.ui.resolution_spinBox.text())
        self.parent.ss_angular_spacing = int(self.ui.angular_spacing_spinBox.text())
        self.parent.update_spiral_search()

    def gpredict_button(self):
        #when gpredict button has been clicked:
        if self.parent.gpredict_connection:
            self.parent.stop_gpredict_socket()
        else:
            self.parent.start_gpredict_socket()
    
    def gpredict_port_update(self):
        self.parent.socket_addr = int(self.ui.gpredict_port_input.text())
    
    def serial_port_update(self):
        self.parent.serial_port_addr = self.ui.serial_port_input.text()

    def raw_target_reset(self):
        self.parent.new_target = 1
        self.parent.raw_target = [0, 0]
        self.ui.raw_tgt_az_label.setText("{:05.1f}".format(self.parent.raw_target[0]))
        self.ui.raw_tgt_el_label.setText("{:04.1f}".format(self.parent.raw_target[1]))

    def man_bt_1(self): #Could probably use a generator of some kind to generate these functions
        self.manual_update_az(100)
    def man_bt_2(self):
        self.manual_update_az(10)
    def man_bt_3(self):
        self.manual_update_az(1)
    def man_bt_4(self):
        self.manual_update_az(0.1)
    def man_bt_5(self):
        self.manual_update_az(-100)
    def man_bt_6(self):
        self.manual_update_az(-10)
    def man_bt_7(self):
        self.manual_update_az(-1)
    def man_bt_8(self):
        self.manual_update_az(-0.1)
    def man_bt_9(self):
        self.manual_update_el(10)
    def man_bt_10(self):
        self.manual_update_el(1)
    def man_bt_11(self):
        self.manual_update_el(0.1)
    def man_bt_12(self):
        self.manual_update_el(-10)
    def man_bt_13(self):
        self.manual_update_el(-1)
    def man_bt_14(self):
        self.manual_update_el(-0.1)

    def manual_update_az(self, val):
        self.parent.new_target = 1
        if (self.parent.manual_target_offset[0] + val) > 180:
            self.parent.manual_target_offset[0] = 180
        elif (self.parent.manual_target_offset[0] + val) < -180:
            self.parent.manual_target_offset[0] = -180
        else:
            self.parent.manual_target_offset[0] += val
        
        if self.parent.manual_target_offset[0] < 0:
            self.ui.manual_offset_az_minus.show()
        else:
            self.ui.manual_offset_az_minus.hide()
        self.ui.manual_offset_az_label.setText("{:05.1f}".format(abs(self.parent.manual_target_offset[0])))
    
    def manual_update_el(self, val):
        self.parent.new_target = 1
        if (self.parent.manual_target_offset[1] + val) > 90:
            self.parent.manual_target_offset[1] = 90
        elif (self.parent.manual_target_offset[1] + val) < -90:
            self.parent.manual_target_offset[1] = -90
        else:
            self.parent.manual_target_offset[1] += val
        if self.parent.manual_target_offset[1] < 0:
            self.ui.manual_offset_el_minus.show()
        else:
            self.ui.manual_offset_el_minus.hide()
        self.ui.manual_offset_el_label.setText("{:04.1f}".format(abs(self.parent.manual_target_offset[1])))

    def serial_button(self):
        if not self.parent.serial_connection:
            self.parent.start_serial_connection()
            self.ui.serial_connect_btn.setText("Close Serial Connection")
            self.ui.serial_state_str.setText("Connected")
        else:
            self.parent.stop_serial_connection()
            self.ui.serial_connect_btn.setText("Open Serial Connection")
            self.ui.serial_state_str.setText("Disconnected")

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
            position = self.parent.sercon.get_position()
            #Then send position to parent
            self.parent.sercon.send_data(b'S') #Arduino get state command
            state = self.parent.sercon.read_data() #Listen for the response for the arduino, then put the response string into state variable
            self.parse_state(state)
    
    def rotate_clockwise(self):
        try:
            if self.parent.serial_connection_enabled:
                #GREY OUT PARTS OF WINDOW DURING ROTATION
                self.parent.sercon.send_data(b'C1')
        except:
            print("ERROR: rotate command not sent")

    #Tharusha Unwind CCW and Unwind CW methods 2023-07-01
    def unwind_ccw(self):
        self.parent.unwind_connection=1
        self.parent.unwind_ccw=1
        self.parent.unwind_counter=0
        print("Unwinding counterclockwise...")
        self.thread = QThread()
        self.worker = ss_Worker(self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.unwind)
        self.thread.start()

    def unwind_stop(self):
        print("Stopped unwinding")
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()

    def unwind_cw(self):
        self.parent.unwind_connection=1
        self.parent.unwind_ccw=0
        self.parent.unwind_counter=0
        print("Unwinding clockwise...")
        self.thread = QThread()
        self.worker = ss_Worker(self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.unwind)
        self.thread.start()

    

class ss_Worker(QObject):
    def __init__(self, mainclass):
        super().__init__()
        self.main = mainclass

    #Tharusha Unwind CCW and Unwind CW threads 2023-07-01
    def unwind(self):
        while self.main.parent.unwind_connection:
            self.main.parent.unwind_counter+=1
            if self.main.parent.unwind_ccw:
                print("unwinding ccw:", self.main.parent.unwind_counter, "degrees")
                self.main.manual_update_az(-1)
            else:
                print("unwinding cw:", self.main.parent.unwind_counter, "degrees")
                self.main.manual_update_az(1)
            time.sleep(0.75)
            

    def run(self):
        for i in range(len(self.main.parent.coords)):
            if self.main.parent.spiral_search_connection:
                self.main.manual_update_az(self.main.parent.coords[i][0])
                self.main.manual_update_el(self.main.parent.coords[i][1])
                if i > 0:
                    if abs(self.main.parent.coords[i][0] - self.main.parent.coords[i-1][0]) > abs(self.main.parent.coords[i][1] - self.main.parent.coords[i-1][1]):
                        time.sleep(0.5*abs(self.main.parent.coords[i][0] - self.main.parent.coords[i-1][0]))
                    else:
                        time.sleep(0.5*abs(self.main.parent.coords[i][1] - self.main.coords[i-1][1]))
            else:
                break
    
    #Tharusha Unwind CCW and Unwind CW stop adjusted 2023-07-01
    def stop(self):
        self.main.parent.spiral_search_connection=0
        self.main.parent.unwind_connection=0



