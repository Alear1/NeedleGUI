#Attaching the socket
#THIS IS GOING TO HAVE TO GO INTO ANOTHER THREAD(MAYBE)

#TODO: Add timeout or cancellation to gpredict connection

import socket
import misc_tools

class SocketGrabber:

    def __init__(self, port=4533, host='127.0.0.1', verbose=0):
        
        self.PORT = port
        self.HOST = host

        self.verbose = verbose

        self.rec_data = None

    def blocking_recv(self):
        try:
            with self.conn:
                print("Connected by", self.addr)
                while True:
                    data = self.conn.recv(4096)
                    print(data)
                    if not data:
                        break
                    self.conn.sendall(b'AZ123.4 EL56.7')
        except:
            print("Error creating connection")
    
    def start_nonblocking(self):
        #Starts the non-blocking gpredict connection

        print("Starting TCP socket on address", self.PORT)

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.HOST, self.PORT))
        except:
            print("Error starting socket in socket_attachment")
            return 0

        try:
            print("Listening for GPredict connection")
            self.socket.listen()
            self.conn, self.addr = self.socket.accept()
            #self.conn.setblocking(0)
        except:
            print("Error listening for socket")
            return 0
            
        self.rec_data = self.conn.recv(4096)
        if not self.rec_data:
            print("Error establishing Gpredict connection")
            self.close_connection()
        else:
            print("Connected by", self.addr)
        self.conn.sendall(b'AZ0 EL0')


    def read_data(self):
        
        try:
            if self.conn.recv(4096):
                raw_data = self.conn.recv(4096)
        except:
            print("Error with reading data")

        if self.verbose: 
            print(self.rec_data)
        
        #Get target tuple from cleaned string:
        if "Z" in self.rec_data:
            raw_data = misc_tools.strip_regex(raw_data)
            self.rec_data = misc_tools.extract_az_el_from_string(self.rec_data)
            return self.rec_data

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
        except:
            print("Error closing Gpredict connection")

    def update_data(self, POSITION):
        #Read current target data from gpredict and send current position data
        #Returns target data

        self.read_data()
        self.write_data()
        return self.rec_data


