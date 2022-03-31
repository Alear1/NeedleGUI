import QtQuick
import QtQuick.Controls
import GSGUI

Rectangle {
    id: base
    width: 1000
    height: 450
    color: "#212121"

    Rectangle {
        id: readouts
        x: 316
        y: 39
        width: 443
        height: 113
        color: "#353535"
        radius: 5
        rotation: 0
        z: 0

        Text {
            id: target_azimuth
            x: 254
            y: 27
            color: "#ffffff"
            text: qsTr("TARGET ELEVATION")
            font.pixelSize: 12

            Text {
                id: text4
                x: 105
                width: 31
                height: 16
                color: "#ffffff"
                text: qsTr("000.00")
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: -45
            }
        }

        Text {
            id: target_elevation
            x: 26
            y: 27
            color: "#ffffff"
            text: qsTr("TARGET AZIMUTH")
            font.pixelSize: 12
            Text {
                id: text5
                x: 105
                width: 31
                height: 16
                color: "#ffffff"
                text: qsTr("000.00")
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: -52
            }
        }

        Text {
            id: azimuth_position1
            x: 254
            y: 68
            color: "#ffffff"
            text: qsTr("AZIMUTH POSITION")
            font.pixelSize: 12
            Text {
                id: text7
                x: 105
                width: 31
                height: 16
                color: "#ffffff"
                text: qsTr("000.00")
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: -40
            }
        }

        Text {
            id: azimuth_position
            x: 26
            y: 68
            color: "#ffffff"
            text: qsTr("AZIMUTH POSITION")
            font.pixelSize: 12
            Text {
                id: text6
                x: 105
                width: 31
                height: 16
                color: "#ffffff"
                text: qsTr("000.00")
                anchors.verticalCenter: parent.verticalCenter
                anchors.right: parent.right
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: -40
            }
        }
    }

    Rectangle {
        id: right_buttons
        x: 781
        y: 39
        width: 145
        height: 373
        color: "#353535"
        radius: 5

        Switch {
            id: gpredict_connector
            x: 42
            y: 8

            Text {
                id: text1
                color: "#ffffff"
                text: qsTr("GPREDICT\nCONNECTOR")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: -20
                anchors.rightMargin: 0
            }
        }

        Switch {
            id: gpredict_serial
            x: 42
            y: 97
            text: qsTr("")

            Text {
                id: text2
                y: 52
                height: 27
                color: "#ffffff"
                text: "GPREDICT\nSERIAL"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: -20
                anchors.rightMargin: 0
            }
        }

        RoundButton {
            id: calibration
            x: 35
            y: 280
            width: 75
            height: 40

            Text {
                id: text3
                color: "#ffffff"
                text: qsTr("CALIBRATION")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: -20
                anchors.rightMargin: 0
                anchors.leftMargin: 0
            }

            Text {
                id: status
                x: 36
                y: 12
                color: "#ffffff"
                text: qsTr("STATUS:")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: -40
                anchors.rightMargin: 0
            }
        }

        Switch {
            id: gpredict_connector1
            x: 42
            y: 187
            Text {
                id: text8
                color: "#ffffff"
                text: qsTr("MOTOR\nON/OFF")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: -20
                anchors.rightMargin: 0
            }
        }
    }

    Rectangle {
        id: manual_control
        x: 316
        y: 171
        width: 443
        height: 120
        color: "#353535"
        radius: 5

        Text {
            id: manual_az_number
            y: 24
            color: "#ffffff"
            text: qsTr("000.00")
            anchors.left: parent.left
            font.letterSpacing: 15
            font.pixelSize: 30
            anchors.leftMargin: 35

            Button {
                id: button
                x: 1
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button1
                x: 1
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button2
                x: 32
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button3
                x: 32
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button4
                x: 64
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button5
                x: 64
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button6
                x: 115
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button7
                x: 115
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button8
                x: 147
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button9
                x: 147
                y: -19
                width: 14
                height: 26
            }

            Text {
                id: manual_az_text
                x: 32
                y: 68
                color: "#ffffff"
                text: qsTr("MANUAL AZIMUTH")
                font.pixelSize: 12
            }
        }

        Text {
            id: manual_az_number1
            x: 247
            y: 24
            color: "#ffffff"
            text: qsTr("000.00")
            anchors.right: parent.right
            font.letterSpacing: 15
            font.pixelSize: 30
            anchors.rightMargin: 35
            Button {
                id: button10
                x: 1
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button11
                x: 1
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button12
                x: 32
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button13
                x: 32
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button14
                x: 64
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button15
                x: 64
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button16
                x: 115
                y: -19
                width: 14
                height: 26
            }

            Button {
                id: button17
                x: 115
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button18
                x: 147
                y: 36
                width: 14
                height: 26
            }

            Button {
                id: button19
                x: 147
                y: -19
                width: 14
                height: 26
            }

            Text {
                id: manual_az_text1
                x: 25
                y: 68
                color: "#ffffff"
                text: qsTr("MANUAL ELEVATION")
                font.pixelSize: 12
            }
        }
    }

    Rectangle {
        id: bottom_buttons
        x: 316
        y: 309
        width: 443
        height: 103
        color: "#353535"
        radius: 5

        TextField {
            id: textField
            y: 61
            height: 45
            color: "#ddffffff"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 114
            anchors.leftMargin: 6
            anchors.bottomMargin: -3
            placeholderTextColor: "#ffffff"
            placeholderText: qsTr("SERIAL INPUT")
        }

        Button {
            id: button20
            x: 8
            y: 14
            width: 158
            height: 48
            text: qsTr("WIND CW")
        }

        Button {
            id: button21
            x: 178
            y: 14
            width: 151
            height: 48
            text: qsTr("WIND CCW")
        }

        Switch {
            id: gpredict_connector2
            x: 359
            y: 14
            Text {
                id: text9
                color: "#ffffff"
                text: qsTr("WIRED/WIRELESS")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: -20
                anchors.rightMargin: 0
            }
        }
    }

    Button {
        id: emergency_stop
        x: 15
        y: 309
        width: 285
        height: 103
        text: qsTr("EMERGENCY STOP")
    }

    Rectangle {
        id: spiral_search
        x: 15
        y: 39
        width: 285
        height: 252
        color: "#353535"
        radius: 5

        Button {
            id: spiral_button
            x: 16
            y: 22
            width: 253
            height: 48
            text: qsTr("SPIRAL SEARCH")
        }

        TextField {
            id: textField1
            x: 16
            y: 103
            width: 253
            height: 46
            color: "#ddffffff"
            placeholderTextColor: "#ffffff"
            placeholderText: qsTr("SPEED")
        }

        TextField {
            id: textField2
            x: 16
            y: 183
            width: 253
            height: 46
            color: "#ddffffff"
            placeholderTextColor: "#ffffff"
            placeholderText: qsTr("RESOLUTION")
        }
    }
}

/*##^##
Designer {
    D{i:0}D{i:3}D{i:2}D{i:5}D{i:4}D{i:7}D{i:6}D{i:9}D{i:8}D{i:1;locked:true}D{i:12}D{i:11}
D{i:14}D{i:13}D{i:16}D{i:17}D{i:15}D{i:19}D{i:18}D{i:10;locked:true}D{i:22}D{i:23}
D{i:24}D{i:25}D{i:26}D{i:27}D{i:28}D{i:29}D{i:30}D{i:31}D{i:32}D{i:21}D{i:34}D{i:35}
D{i:36}D{i:37}D{i:38}D{i:39}D{i:40}D{i:41}D{i:42}D{i:43}D{i:44}D{i:33}D{i:20;locked:true}
D{i:46}D{i:47}D{i:48}D{i:50}D{i:49}D{i:45;locked:true}D{i:51;locked:true}D{i:53}D{i:54}
D{i:55}D{i:52}
}
##^##*/

