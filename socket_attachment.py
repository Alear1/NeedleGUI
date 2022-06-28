#Attaching the socket
#https://realpython.com/python-sockets/

#TODO: Add timeout or cancellation to gpredict connection

import socket
import misc_tools
import threading
import time

class SocketGrabber:

    def __init__(self, parent, port=4533, host='127.0.0.1', verbose=0):
        super(SocketGrabber, self).__init__()
        
        self.parent = parent
        self.PORT = port
        self.HOST = host

        self.verbose = verbose

        self.rec_data = None
        self.exit_flag = 0

    def blocking_recv(self):

        print("Starting TCP socket on address", self.PORT)

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('self.socket:', self.socket)
            self.socket.settimeout(60)
            print('Host:', self.HOST, '|| Port:', self.PORT)
            self.socket.bind((self.HOST, self.PORT))
        except:
            print("Error starting socket in socket_attachment")
            return 0
        
        try:
            print("Listening for GPredict connection")
            self.socket.listen()
            self.conn, self.addr = self.socket.accept()
            self.socket.settimeout(None)
            print("Starting attempt")
            with self.conn:
                print("Connected by", self.addr)
                self.parent.gpredict_connection = 1
                while True and not self.exit_flag and self.parent.socket_connection_enabled:
                    data = self.conn.recv(4096)
                    if not data:
                        break
                    self.conn.sendall(self.parent.create_socket_send_string())
                    self.parse_data(data)
                self.close_connection()
        except:
            print("Gpredict connection timeout")
            self.parent.gpredict_connection = 0
            self.parent.socket_connection_enabled = 0

    def parse_data(self, input_data):
        data = input_data.decode("UTF-8")
        try:
            if data[0] == "P":
                #New target given
                self.parent.new_target = 1
                #Remove command char:
                data = data[2:].strip()
                #find first space:
                index = data.index(" ")
                #extract AZ target data
                self.parent.raw_target[0] = float(data[0:index])
                #remove az data and spaces:
                data = data[index + 1:].strip()
                self.parent.raw_target[1] = float(data)
        except:
            self.parent.raw_target[1] = 0
            print("ERROR in parse_data")

    def write_data(self, output_string):
        #Sends data to gpredict over socket
        try:
            self.conn.sendall(bytes(output_string, 'utf-8'))
            return 1
        except:
            print("Error writing data")
            return 0

    def close_connection(self):
        print("Closing Gpredict connection")
        try:
            self.conn.close()
            self.socket.close()
            self.parent.socket_connection_enabled = 0
            self.parent.gpredict_connection = 0

        except:
            print("Error closing Gpredict connection")

    def update_data(self, POSITION):
        #Read current target data from gpredict and send current position data
        #Returns target data

        self.read_data()
        self.write_data()
        return self.rec_data

class SocketThread(threading.Thread):
    def __init__(self, threadID, name, counter, socket):
        super(SocketThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.exit_flag = 0
        self.sock = socket
    
    def run(self):
        print ("Starting " + self.name)
        self.sock.blocking_recv()
        print ("Exiting " + self.name)