# NeedleGUI

Inputs:
- start/stop gpredict connection
- start/stop arduino connection
- Manual offset az & el
- Gpredict connection port
- Serial connection address
- set current position as x & y, az & el
- one az rotation CCW
- one az rotation CW
- Spiral search tool
- Emergency Stop
- Turn motors off
- Manual Serial message input

Displays:
- Gpredict connection state
- Serial connection state
- Gpredict connection port
- Serial connection address
- Target from Gpredict az & el
- Position from Arduino  az & el
- Manual offset az & el
- set current position as x & y, az & el
- currently rotating CCW
- currently rotating CW
- currently spiral searching
- emergency stopped
- motors off

Possible Functions:
- Set motor speed
- Set motor control type
- Temperature output
- Calibrate
- 


To add a new state variable to the list:
- Create a new button/value/whatever in the designer
- Create a function in gui_main.py that handles the button/value/whatever, and adds a new message to the serial_msg_queue
- Connect the button to the function in the init of gui_main.py
- Write the handler for the new message into the arduino, such that it outputs the correct order and values in the state string
- Add the new state variable to the self.state_varables dict in data_handler.py. make sure the order is correct.

NOTE:
You can send whatever messages you want to the arduino, but it will only ever respond with position or state strings

Position string out of arduino looks like: b"AZ123.4 EL56.7"

State string out of arduino looks like: b"S 0 0 0 23.5 1", the order corresponds to the state_variables dict. The S designates that this is a state string and the order of the numbers will be assigned to the state_variables dict. The number of keys in the state_variables dict MUST be the same as the number of elements in the state string, minus the S at the front. NON-NUMERICAL VALUES NOT ALLOWED
