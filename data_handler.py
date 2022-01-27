#Handles the data 

import serial_connector
import socket_attachment
import os

class CoreInfo:
    def __init__(self):
        
        #Define pointing information (target and current) (az and el will be float tuples)
        self.current_target = (0, 0)
        self.current_position = (0, 0)
        self.manual_target_offset = (0,0)
        self.manual_position_offset = (0, 0)

        #Define other data(??)

        self.socket_adddr = None
        self.serial_port_addr = None
        
        #Other objects:
        self.sock = None
        

    
    def start_gpredict_socket(self):
        self.sock = socket_attachment.socketgrabber()