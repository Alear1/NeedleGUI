#Connects to the nano over serial
#https://pyserial.readthedocs.io/en/latest/shortintro.html


#TODO: in init, create port detection

import serial
import misc_tools
import threading
import weakref

class SerialHandler:
    def __init__(self, parent, PORT=None, BAUDRATE=9600):
        
        self.parent = weakref.ref(parent)

        if PORT:
            pass
            self.ser = serial.Serial()
            self.ser.baudrate = BAUDRATE
            self.ser.port = PORT

        else:
            pass
            #run port detection to detect arduino somehow

        self.exit_flag = 0
        self.in_data = None
        self.target = [0, 0]
        self.position = [0, 0]

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

    def comm_loop(self):
        #Every full second the get position command is sent to the Arduino
        #Other commands can be sent when this is not happening (async is a nightmare)
        pass

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
        while not self.exit_flag:
            try:
                if self.ser.is_open:
                    return self.ser.readline()
                else:
                    raise Exception()
            except:
                print("Error reading data from serial connection")
                return None
    
    def read_loop(self):
        
        while not self.exit_flag:
            
            self.ser.write(bytes(misc_tools.az_el_to_string(self.position), 'utf-8'))

class SerialThread(threading.Thread):
    def __init__(self, threadID, name, counter, serial):
        super(SerialThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.exit_flag = 0
        self.ser = serial
    
    def run(self):
        print ("Starting " + self.name)
        self.ser.start_connection()
        self.ser.comm_loop()
        print ("Exiting " + self.name)