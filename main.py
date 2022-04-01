#main test folder
#In the GUI the user can initialize the connection to gpredict or to the serial port

#Data to/from gpredict will come through socket_attachment to the datahandler
#Data to/from the arduino will come through serial_connector to the datahandler

#All the active data will get held onto by the datahandler

#http://www.w1npp.org/events/2010/2010-f~1/SATELL~1/GPREDI~1.PDF

import data_handler

if __name__ == "__main__":
    
    #Start the gui and initialize the data handler
    print("Starting NeedleGUI")
    core_info = data_handler.CoreInfo()
    core_info.start_gui()
    print("Exiting NeedleGUI. Goodbye!")
    #Testing Both:
    #core_info.start_gpredict_socket()
    #core_info.start_serial_connection()

    #Testing the serial connection:
    #ser = serial_connector.SerialHandler(PORT="/dev/ttyUSB0")
    #ser.manual_input()
    #ser.close_connection()

   #Testing socket:
    #core_info.start_gpredict_socket()
    #core_info.stop_gpredict_socket()