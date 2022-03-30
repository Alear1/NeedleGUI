# NeedleGUI

-Commands that can be sent to the Arduino:
-Set position
-Get position
-clockwise full rotation
-anticlockwise full rotation
-start spiral
-get temperature


Data that can be received from Arduino:
-Current Position
-State data  #NEED TO FIND A WAY TO PARSE THIS

Arduino communication method:
Send command -> wait -> receive response(if required)

Ex:
for set position
Send |SET POSITION(az/el)| -> wait -> Send |GET POSITION| -> wait -> Receive |POSITION|
