#Connects to the nano over serial
#https://pyserial.readthedocs.io/en/latest/shortintro.html


#TODO: in init, create port detection

import serial
import time
import misc_tools
import threading

class SerialHandler:
    def __init__(self, parent, PORT=None, BAUDRATE=9600):
        
        self.parent = parent

        if PORT:
            pass
            self.ser = serial.Serial()
            self.ser.baudrate = BAUDRATE
            self.ser.port = PORT
            self.ser.timeout = 1

        else:
            pass
            #run port detection to detect arduino somehow

        self.timeout = 0.1

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
            self.parent.serial_connection = 0
            self.parent.serial_connection_enabled  = 0
            return 0

    def close_connection(self):
        self.ser.close()
        if self.ser.is_open:
            print("WARNING: SERIAL CONNECTION NOT CLOSED")
        else:
            self.parent.serial_connection_enabled = 0
            self.parent.serial_connection = 0
            print("Serial connection closed")

    def manual_input(self):
        sdata = None
        print("Send the letter Q to quit manual mode")
        while sdata != "Q":
            sdata = input()
            self.ser.write(bytes(sdata, 'utf-8'))
            print(self.ser.readline())

    def comm_loop(self):
        #Loop that the serial thread sits in. loops until it gets a message in the serial_msg_queue
        #Once a message is in the serial_msg_queue it will send over serial. Waits for response from arduino
        self.parent.serial_connection = 1
        rx_data = None
        while self.parent.serial_connection_enabled and self.ser.is_open:
            try:
                if len(self.parent.serial_msg_queue) > 0:
                    self.send_data(self.parent.serial_msg_queue[0]) #send 0th element in message queue
                    if self.parent.serial_msg_queue[0][2] != " " or self.parent.serial_msg_queue[0][0] == "S":
                        rx_data = None
                    else:
                        rx_data = self.read_data() #read data from serial connection if there is a response
                    self.parent.serial_msg_queue.pop(0) #remove 0th element in message queue
                
                    if rx_data is not None:
                        rx_data = rx_data.decode("UTF-8")
                        #The only thing that the gui will receive from the serial connection will be position or state information
                        #print(rx_data)
                        try:
                            if rx_data[0] == "A":
                                self.parent.raw_position = misc_tools.extract_az_el_from_string(rx_data)
                            elif rx_data[0] == "S":
                                self.parse_state(rx_data)
                            else:
                                # print("WARNING: unrecognized response from connected serial device")
                                pass
                        except:
                            # print("ERROR: received null response from serial device")
                            pass

                time.sleep(0.001)
            except:
                self.close_connection()
        self.close_connection()       

    def parse_state(self, data):
        #Parses and updates all the state variables

        #first remove the S and initial space:
        data = data[2:]
        try:
            for key in self.parent.state_variables:
                index = data.index(" ")
                info = data[0 : index]
                self.parent.state_variables[key] = float(info)
                data = data[index + 1:]
        except ValueError:
            info = data
            self.parent.state_variables[key] = float(info)
            data = data[index + 1:]
        except:
            print("Warning: serial state response parsing failed")

    def send_data(self, msg):
        #takes a message string and converts to bytes, then sends over serial connection
        #returns 1 if successful and 0 if failed
        print('msg:', msg)
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

        d = self.ser.readline()
        for a in range(0, 10):
            time.sleep(self.timeout)    #"Timeout" should be determined by number of messages with no response? but some messages have no response so...
            
        try:
            if self.ser.is_open:
                return d
            else:
                raise Exception()
        except:
            print("Error reading data from serial connection")
            return None
    
    def get_position(self):
        self.send_data(b'AZ EL')
        time.sleep(0.1)
        in_data = self.read_data()
        self.parent.raw_position = misc_tools.extract_az_el_from_string(in_data)

class SerialThread(threading.Thread):
    def __init__(self, threadID, name, counter, serial):
        super(SerialThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.ser = serial
    
    def run(self):
        print ("Starting " + self.name)
        self.ser.start_connection()
        self.ser.comm_loop()
        print ("Exiting " + self.name)