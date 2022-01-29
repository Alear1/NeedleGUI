#Handles the data 

import serial_connector
import socket_attachment
import os

class CoreInfo:
    def __init__(self):
        
        #Define pointing information (target and current) (az and el will be float tuples)
        self.raw_target = (0, 0)
        self.raw_position = (0, 0)
        self.manual_target_offset = (0,0)
        self.manual_position_offset = (0, 0)

        self.current_target = self.raw_target
        self.current_position = self.current_target
        
        #Data required to create gpredict connection:
        self.socket_adddr = 4533
        self.socket_host = '127.0.0.1'

        #Data required to create serial connection:
        self.serial_port_addr = None
        self.serial_port_baudrate = 9600

        #is there currently a connection to Gpredict?
        self.gpredict_connection = 0
        #is there currently a connection to the serial port?
        self.serial_connection = 0
        
    
    def update(self):
        #This will update the back end

        try:
            self.current_target = self.sockcon.update_data(self.current_position)
            self.sercon.update_data()
        except:
            print("ERROR: Could not update")

    def start_gpredict_socket(self):
        #Start socket connection

        self.sockcon = socket_attachment.SocketGrabber(self.socket_addr, self.serial_port_addr)
        if self.sockcon.start_nonblocking():
            print("Gpredict connection created successfully")
            self.gpredict_connection = 1
            return 1
        else:
            print("Gpredict connection failed")
            self.gpredict_connection = 0
            return 0

    def start_serial_connection(self):
        #Start serial connection

        self.sercon = serial_connector.SerialHandler(PORT=self.serial_port_addr, BAUDRATE=self.serial_port_baudrate)
        if self.sercon.start_connection():
            print("Serial connection established")
            self.serial_connection = 1
            return 1
        else:
            print("Serial connection failed")
            self.serial_connection = 0
            return 0
