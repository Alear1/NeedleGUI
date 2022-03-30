#GUI handler for NeedleGUI using tkinter
#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

import threading
import weakref
import time

class MainWindow:
    def __init__(self, parent):
        #Initialize all the required stuff for QT here

        self.parent = weakref.ref(parent)   #This is the data handler object
        
        #Examples:
        self.window.title('NeedleGUI')
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        self.draw_statics()
    
    def window_loop(self):
        #This is where the main loop of the window lives
        while True: #This should end up being while alive or sth like that
            self.update()
            position = self.parent.sercon.get_position()
            #Then send position to parent
            self.parent.sercon.send_data(b'S') #Arduino get state command
            state = self.parent.sercon.read_data() #Listen for the response for the arduino, then put the response string into state variable
            self.parse_state(state)

    def update(self):
        time.sleep(0.0001)
    
    def rotate_clockwise(self):
        try:
            if self.parent.serial_connection_enabled:
                #GREY OUT PARTS OF WINDOW DURING ROTATION
                self.parent.sercon.send_data(b'C1')
        except:
            print("ERROR: rotate command not sent")

    def parse_state(self, msg):
        #use space as delimiter to split string into individual sections
        #parse individual parts of string
        #send data to parent aka data handler
        #ideally scalable, takes a dict with position in string and corresponding variable
        pass

    #Start Gpredict Connection:
    #self.parent.start_gpredict_socket()
    #Stop Gpredict Connection:
    #self.parent.socket_connection_enabled = 0

    #Start Arduino Connection:
    #self.parent.serial_connection_enabled = 1
    #self.parent.serial_connection_enabled = 0