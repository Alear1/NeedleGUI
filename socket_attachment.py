#Attaching the socket
#THIS IS GOING TO HAVE TO GO INTO ANOTHER THREAD(MAYBE)

import socket

class SocketGrabber:

    def __init__(self, port=4533, host='127.0.0.1'):
        
        self.PORT = port
        self.HOST = host

        print("Starting TCP socket on address", self.PORT)

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.HOST, self.PORT))
        except:
            print("Error starting socket in socket_attachment")

        try:
            print("Listening for GPredict connection")
            self.socket.listen()
            self.conn, self.addr = self.socket.accept()
        except:
            print("Error listening for socket")

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
        
        self.rec_data = self.conn.recv(4096)
        if not self.rec_data:
            print("Error establishing Gpredict connection")
            self.close_connection()
        else:
            print("Connected by", self.addr)

    def read_data(self, verbose=False):
        self.rec_data = self.conn.recv(4096)

        if verbose:
            print(self.rec_data)
        else:
            return self.rec_data

    def close_connection(self):
        print("Closing Gpredict connection")
        try:
            self.conn.close()
            self.socket.close()
        except:
            print("Error closing Gpredict connection")