#Connects to the nano over serial
#https://pyserial.readthedocs.io/en/latest/shortintro.html


#TODO: in init, create port detection

import serial

class SerialHandler:
    def __init__(self, PORT=None, BAUDRATE=9600):
        
        if PORT:
            pass
            self.ser = serial.Serial()
            self.ser.baudrate = BAUDRATE
            self.ser.port = PORT

        else:
            pass
            #run port detection to detect arduino somehow


    def start_connection(self):
        try:
            self.ser.open()
            if self.ser.is_open:
                print("Serial connection established")
                return 1
            else:
                raise Exception()
        except:
            print("Error opening serial connection")
            return 0
    
    def close_connection(self):
        self.ser.close()
        if self.ser.is_open:
            print("WARNING: SERIAL CONNECTION NOT CLOSED")
        else:
            print("Serial connection closed")

    def manual_input(self):
        sdata = None
        print("Send the letter Q to quit manual mode")
        while sdata != "Q":
            sdata = input()
            self.ser.write(bytes(sdata, 'utf-8'))
            print(self.ser.readline())

    def send_data(self, msg):
        #takes a message string and converts to bytes, then sends over serial connection
        #returns 1 if successful and 0 if failed
        try:
            bmsg = bytes(msg, 'utf-8')
            if self.ser.is_open:
                self.ser.write(bmsg)
                return 1
            else:
                raise Exception()
        except:
            print("Error sending data through serial connection")
            return 0

    def read_data(self):
        #returns the output of self.ser.readline()
        try:
            if self.ser.is_open:
                return self.ser.readline()
            else:
                raise Exception()
        except:
            print("Error reading data from serial connection")
            return None

