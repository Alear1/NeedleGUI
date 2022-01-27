#GUI handler for NeedleGUI using tkinter
#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

import tkinter as tk

class MainWindow:
    def __init__(self, data):

        self.data = data
        self.window = tk.Tk()

        self.window.title('NeedleGUI')
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        self.draw_statics()

    def draw_statics(self):
        self.lbl=tk.Label(self.window, text="NeedleGUI", fg='black', font=("Terminal", 12))
        self.lbl.place(x=5, y=5)
        
        self.window.mainloop()
        

    def start_gpredict_connection(self):
        #Use the datahandler to start the gpredict socket
        self.data.start_gpredict_socket()
    