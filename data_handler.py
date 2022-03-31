#Handles the data 

import serial_connector
import socket_attachment
import gui_main
import threading
import os

class CoreInfo:
    def __init__(self):
        
        #Define pointing information (target and current) (az and el will be float tuples)
        #standard is [az, el]
        self.raw_target = [0, 0]
        self.raw_position = [0, 0]
        self.manual_target_offset = [0,0]
        self.manual_position_offset = [0, 0]

        self.current_target = self.raw_target + self.manual_target_offset
        self.current_position = self.raw_position + self.manual_position_offset
        
        #Data required to create gpredict connection:
        self.socket_addr = 4533
        self.socket_host = '127.0.0.1'
        self.socket_connection_enabled = 1 #SHOULD BE 0 BY DEFAULT WHEN GUI IS WORKING

        #Data required to create serial connection:
        self.serial_port_addr = '/dev/ttyUSB0'
        self.serial_port_baudrate = 9600
        self.serial_connection_enabled = 1  #SHOULD BE 0 BY DEFAULT WHEN GUI IS WORKING

        #is there currently a connection to Gpredict?
        self.gpredict_connection = 0
        #is there currently a connection to the serial port?
        self.serial_connection = 0    

    def start_gui(self):
        #Start the gui. The gui main loop is the main thread.
        self.gui = gui_main.MainWindow(self)

#THREADS WILL UPDATE INDEPENDENTLY

    #def update(self):
        #This will update the back end

      #  try:
      #      self.current_target = self.sockcon.update_data()
       #     self.sercon.update_data()
        #except:
         #   print("ERROR: Could not update")

    def create_socket_send_string(self):
        #Uses current_position to create a string in byte form that is sent to gpredict
        try:
            #out_string = "AZ" + str(self.current_position[0]) + " EL" + str(self.current_position[1])
            #out_string = out_string.encode('UTF-8')
            out_string = b"p 12.30 4.50\x0a"
            return out_string
        except:
            print("ERROR CREATING SOCKET STRING")
            return b'AZ0 EL0'

    def start_gpredict_socket(self):
        #Start socket connection, should be activated from the gui object

        self.sockcon = socket_attachment.SocketGrabber(self, self.socket_addr, self.socket_host)
        self.sock_thread = socket_attachment.SocketThread(1, "Socket-Thread", 1, self.sockcon)
        self.sock_thread.start()
        self.socket_connection_enabled = 1

    def stop_gpredict_socket(self):
        self.socket_connection_enabled = 0
        self.sock_thread.join()

        #To close the socket set self.socket_connection_enabled = 0. Socket closes itself

    def start_serial_connection(self):
        #Start serial connection, should be activated from the gui object

        self.sercon = serial_connector.SerialHandler(self, PORT=self.serial_port_addr, BAUDRATE=self.serial_port_baudrate)
        self.ser_thread = serial_connector.SerialThread(2, "Serial-Thread", 2, self.sercon)
        self.ser_thread.start()
        self.serial_connection_enabled = 1
    
    def stop_serial_connection(self):
        self.socket_connection_enabled = 0
        self.ser_thread.join()