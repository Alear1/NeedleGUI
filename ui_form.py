# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NeedleGUI_ui_form_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 570))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 570))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.connections = QtWidgets.QGroupBox(self.centralwidget)
        self.connections.setMaximumSize(QtCore.QSize(200, 16777215))
        self.connections.setFlat(False)
        self.connections.setCheckable(False)
        self.connections.setObjectName("connections")
        self.formLayout = QtWidgets.QFormLayout(self.connections)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gpredict_port_label = QtWidgets.QLabel(self.connections)
        self.gpredict_port_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gpredict_port_label.setObjectName("gpredict_port_label")
        self.gridLayout_2.addWidget(self.gpredict_port_label, 2, 0, 1, 1)
        self.gstate_label = QtWidgets.QLabel(self.connections)
        self.gstate_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gstate_label.setObjectName("gstate_label")
        self.gridLayout_2.addWidget(self.gstate_label, 0, 0, 1, 1)
        self.serial_label = QtWidgets.QLabel(self.connections)
        self.serial_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.serial_label.setObjectName("serial_label")
        self.gridLayout_2.addWidget(self.serial_label, 1, 0, 1, 1)
        self.serial_port_input = QtWidgets.QLineEdit(self.connections)
        self.serial_port_input.setObjectName("serial_port_input")
        self.gridLayout_2.addWidget(self.serial_port_input, 3, 1, 1, 1)
        self.gpredict_state_str = QtWidgets.QLabel(self.connections)
        self.gpredict_state_str.setObjectName("gpredict_state_str")
        self.gridLayout_2.addWidget(self.gpredict_state_str, 0, 1, 1, 1)
        self.serial_port_label = QtWidgets.QLabel(self.connections)
        self.serial_port_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.serial_port_label.setObjectName("serial_port_label")
        self.gridLayout_2.addWidget(self.serial_port_label, 3, 0, 1, 1)
        self.gpredict_port_input = QtWidgets.QLineEdit(self.connections)
        self.gpredict_port_input.setObjectName("gpredict_port_input")
        self.gridLayout_2.addWidget(self.gpredict_port_input, 2, 1, 1, 1)
        self.serial_state_str = QtWidgets.QLabel(self.connections)
        self.serial_state_str.setObjectName("serial_state_str")
        self.gridLayout_2.addWidget(self.serial_state_str, 1, 1, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gpredict_connect_btn = QtWidgets.QPushButton(self.connections)
        self.gpredict_connect_btn.setObjectName("gpredict_connect_btn")
        self.verticalLayout_3.addWidget(self.gpredict_connect_btn)
        self.serial_connect_btn = QtWidgets.QPushButton(self.connections)
        self.serial_connect_btn.setObjectName("serial_connect_btn")
        self.verticalLayout_3.addWidget(self.serial_connect_btn)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_3)
        self.gridLayout_6.addWidget(self.connections, 0, 2, 4, 1)
        self.spiral_search = QtWidgets.QGroupBox(self.centralwidget)
        self.spiral_search.setObjectName("spiral_search")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.spiral_search)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 30, 231, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.resolution_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.resolution_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resolution_label.setObjectName("resolution_label")
        self.gridLayout.addWidget(self.resolution_label, 2, 0, 1, 1)
        self.resolution_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.resolution_input.setObjectName("resolution_input")
        self.gridLayout.addWidget(self.resolution_input, 2, 1, 1, 1)
        self.speed_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.speed_input.setObjectName("speed_input")
        self.gridLayout.addWidget(self.speed_input, 0, 1, 1, 1)
        self.speed_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.speed_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speed_label.setObjectName("speed_label")
        self.gridLayout.addWidget(self.speed_label, 0, 0, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search_button.setCheckable(False)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.searching_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.searching_label.setAlignment(QtCore.Qt.AlignCenter)
        self.searching_label.setObjectName("searching_label")
        self.verticalLayout.addWidget(self.searching_label)
        self.gridLayout_6.addWidget(self.spiral_search, 0, 0, 4, 1)
        self.motor_state = QtWidgets.QGroupBox(self.centralwidget)
        self.motor_state.setObjectName("motor_state")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.motor_state)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 231, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.enabled_state_el_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.enabled_state_el_btn.setObjectName("enabled_state_el_btn")
        self.gridLayout_5.addWidget(self.enabled_state_el_btn, 1, 1, 1, 1)
        self.enabled_state_az_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.enabled_state_az_btn.setObjectName("enabled_state_az_btn")
        self.gridLayout_5.addWidget(self.enabled_state_az_btn, 1, 0, 1, 1)
        self.enabled_state_az_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.enabled_state_az_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enabled_state_az_label.setObjectName("enabled_state_az_label")
        self.gridLayout_5.addWidget(self.enabled_state_az_label, 0, 0, 1, 1)
        self.enabled_state_el_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.enabled_state_el_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enabled_state_el_label.setObjectName("enabled_state_el_label")
        self.gridLayout_5.addWidget(self.enabled_state_el_label, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.motor_state, 7, 0, 4, 1)
        self.emergency_stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.emergency_stop_btn.setMinimumSize(QtCore.QSize(10, 160))
        self.emergency_stop_btn.setObjectName("emergency_stop_btn")
        self.gridLayout_6.addWidget(self.emergency_stop_btn, 6, 2, 1, 1)
        self.coordinate_viewer = QtWidgets.QGroupBox(self.centralwidget)
        self.coordinate_viewer.setObjectName("coordinate_viewer")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.coordinate_viewer)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.coord_viewer_az_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.coord_viewer_az_label.setFrameShape(QtWidgets.QFrame.Box)
        self.coord_viewer_az_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.coord_viewer_az_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.coord_viewer_az_label.setObjectName("coord_viewer_az_label")
        self.gridLayout_7.addWidget(self.coord_viewer_az_label, 0, 4, 1, 6)
        self.el_offset_tendn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.el_offset_tendn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.el_offset_tendn_btn.setObjectName("el_offset_tendn_btn")
        self.gridLayout_7.addWidget(self.el_offset_tendn_btn, 7, 12, 1, 1)
        self.manual_offset_layout = QtWidgets.QHBoxLayout()
        self.manual_offset_layout.setObjectName("manual_offset_layout")
        self.manual_offset_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.manual_offset_label.setMaximumSize(QtCore.QSize(123, 16777215))
        self.manual_offset_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.manual_offset_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.manual_offset_label.setObjectName("manual_offset_label")
        self.manual_offset_layout.addWidget(self.manual_offset_label)
        self.manual_offset_az_minus = QtWidgets.QLabel(self.coordinate_viewer)
        self.manual_offset_az_minus.setMaximumSize(QtCore.QSize(20, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.manual_offset_az_minus.setFont(font)
        self.manual_offset_az_minus.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.manual_offset_az_minus.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.manual_offset_az_minus.setObjectName("manual_offset_az_minus")
        self.manual_offset_layout.addWidget(self.manual_offset_az_minus)
        self.manual_offset_az_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.manual_offset_az_label.setMaximumSize(QtCore.QSize(150, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.manual_offset_az_label.setFont(font)
        self.manual_offset_az_label.setAlignment(QtCore.Qt.AlignCenter)
        self.manual_offset_az_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.manual_offset_az_label.setObjectName("manual_offset_az_label")
        self.manual_offset_layout.addWidget(self.manual_offset_az_label)
        self.manual_offset_el_minus = QtWidgets.QLabel(self.coordinate_viewer)
        self.manual_offset_el_minus.setMaximumSize(QtCore.QSize(20, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.manual_offset_el_minus.setFont(font)
        self.manual_offset_el_minus.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.manual_offset_el_minus.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.manual_offset_el_minus.setObjectName("manual_offset_el_minus")
        self.manual_offset_layout.addWidget(self.manual_offset_el_minus)
        self.manual_offset_el_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.manual_offset_el_label.setEnabled(True)
        self.manual_offset_el_label.setMaximumSize(QtCore.QSize(115, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.manual_offset_el_label.setFont(font)
        self.manual_offset_el_label.setAlignment(QtCore.Qt.AlignCenter)
        self.manual_offset_el_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.manual_offset_el_label.setObjectName("manual_offset_el_label")
        self.manual_offset_layout.addWidget(self.manual_offset_el_label)
        self.gridLayout_7.addLayout(self.manual_offset_layout, 6, 0, 1, 16)
        self.raw_pos_layout = QtWidgets.QHBoxLayout()
        self.raw_pos_layout.setObjectName("raw_pos_layout")
        self.raw_pos_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.raw_pos_label.setMaximumSize(QtCore.QSize(120, 50))
        self.raw_pos_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.raw_pos_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.raw_pos_label.setObjectName("raw_pos_label")
        self.raw_pos_layout.addWidget(self.raw_pos_label)
        self.raw_pos_az_label = QtWidgets.QLabel(self.coordinate_viewer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.raw_pos_az_label.setFont(font)
        self.raw_pos_az_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.raw_pos_az_label.setMidLineWidth(10)
        self.raw_pos_az_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_pos_az_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.raw_pos_az_label.setObjectName("raw_pos_az_label")
        self.raw_pos_layout.addWidget(self.raw_pos_az_label)
        self.raw_pos_el_label = QtWidgets.QLabel(self.coordinate_viewer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.raw_pos_el_label.setFont(font)
        self.raw_pos_el_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_pos_el_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.raw_pos_el_label.setObjectName("raw_pos_el_label")
        self.raw_pos_layout.addWidget(self.raw_pos_el_label)
        self.gridLayout_7.addLayout(self.raw_pos_layout, 1, 0, 1, 16)
        self.sent_tgt_layout = QtWidgets.QHBoxLayout()
        self.sent_tgt_layout.setObjectName("sent_tgt_layout")
        self.sent_tgt_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.sent_tgt_label.setMaximumSize(QtCore.QSize(108, 16777215))
        self.sent_tgt_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sent_tgt_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sent_tgt_label.setObjectName("sent_tgt_label")
        self.sent_tgt_layout.addWidget(self.sent_tgt_label)
        self.sent_tgt_az_label = QtWidgets.QLabel(self.coordinate_viewer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.sent_tgt_az_label.setFont(font)
        self.sent_tgt_az_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sent_tgt_az_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sent_tgt_az_label.setObjectName("sent_tgt_az_label")
        self.sent_tgt_layout.addWidget(self.sent_tgt_az_label)
        self.sent_tgt_el_label = QtWidgets.QLabel(self.coordinate_viewer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.sent_tgt_el_label.setFont(font)
        self.sent_tgt_el_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sent_tgt_el_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sent_tgt_el_label.setObjectName("sent_tgt_el_label")
        self.sent_tgt_layout.addWidget(self.sent_tgt_el_label)
        self.gridLayout_7.addLayout(self.sent_tgt_layout, 8, 0, 1, 16)
        self.auto_offset_layout = QtWidgets.QHBoxLayout()
        self.auto_offset_layout.setContentsMargins(-1, -1, -1, 0)
        self.auto_offset_layout.setSpacing(0)
        self.auto_offset_layout.setObjectName("auto_offset_layout")
        self.auto_offset_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.auto_offset_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.auto_offset_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.auto_offset_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.auto_offset_label.setObjectName("auto_offset_label")
        self.auto_offset_layout.addWidget(self.auto_offset_label)
        self.auto_offset_az_minus = QtWidgets.QLabel(self.coordinate_viewer)
        self.auto_offset_az_minus.setEnabled(True)
        self.auto_offset_az_minus.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.auto_offset_az_minus.setFont(font)
        self.auto_offset_az_minus.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.auto_offset_az_minus.setIndent(0)
        self.auto_offset_az_minus.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.auto_offset_az_minus.setObjectName("auto_offset_az_minus")
        self.auto_offset_layout.addWidget(self.auto_offset_az_minus)
        self.auto_offset_az_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.auto_offset_az_label.setMaximumSize(QtCore.QSize(150, 115))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.auto_offset_az_label.setFont(font)
        self.auto_offset_az_label.setAlignment(QtCore.Qt.AlignCenter)
        self.auto_offset_az_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.auto_offset_az_label.setObjectName("auto_offset_az_label")
        self.auto_offset_layout.addWidget(self.auto_offset_az_label)
        self.auto_offset_el_minus = QtWidgets.QLabel(self.coordinate_viewer)
        self.auto_offset_el_minus.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.auto_offset_el_minus.setFont(font)
        self.auto_offset_el_minus.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.auto_offset_el_minus.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.auto_offset_el_minus.setObjectName("auto_offset_el_minus")
        self.auto_offset_layout.addWidget(self.auto_offset_el_minus)
        self.auto_offset_el_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.auto_offset_el_label.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.auto_offset_el_label.setFont(font)
        self.auto_offset_el_label.setAlignment(QtCore.Qt.AlignCenter)
        self.auto_offset_el_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.auto_offset_el_label.setObjectName("auto_offset_el_label")
        self.auto_offset_layout.addWidget(self.auto_offset_el_label)
        self.gridLayout_7.addLayout(self.auto_offset_layout, 3, 0, 1, 16)
        self.raw_tgt_layout = QtWidgets.QHBoxLayout()
        self.raw_tgt_layout.setObjectName("raw_tgt_layout")
        self.raw_tgt_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.raw_tgt_label.setMaximumSize(QtCore.QSize(120, 50))
        self.raw_tgt_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.raw_tgt_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.raw_tgt_label.setObjectName("raw_tgt_label")
        self.raw_tgt_layout.addWidget(self.raw_tgt_label)
        self.raw_tgt_az_label = QtWidgets.QLabel(self.coordinate_viewer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.raw_tgt_az_label.setFont(font)
        self.raw_tgt_az_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_tgt_az_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.raw_tgt_az_label.setObjectName("raw_tgt_az_label")
        self.raw_tgt_layout.addWidget(self.raw_tgt_az_label)
        self.raw_tgt_el_label = QtWidgets.QLabel(self.coordinate_viewer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.raw_tgt_el_label.setFont(font)
        self.raw_tgt_el_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_tgt_el_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.raw_tgt_el_label.setObjectName("raw_tgt_el_label")
        self.raw_tgt_layout.addWidget(self.raw_tgt_el_label)
        self.gridLayout_7.addLayout(self.raw_tgt_layout, 2, 0, 1, 16)
        self.az_offset_tenthdn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_tenthdn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_tenthdn_btn.setObjectName("az_offset_tenthdn_btn")
        self.gridLayout_7.addWidget(self.az_offset_tenthdn_btn, 7, 9, 1, 1)
        self.el_offset_tenthup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.el_offset_tenthup_btn.sizePolicy().hasHeightForWidth())
        self.el_offset_tenthup_btn.setSizePolicy(sizePolicy)
        self.el_offset_tenthup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.el_offset_tenthup_btn.setObjectName("el_offset_tenthup_btn")
        self.gridLayout_7.addWidget(self.el_offset_tenthup_btn, 5, 14, 1, 1)
        self.az_offset_tendn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_tendn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_tendn_btn.setObjectName("az_offset_tendn_btn")
        self.gridLayout_7.addWidget(self.az_offset_tendn_btn, 7, 7, 1, 1)
        self.az_offset_onedn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_onedn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_onedn_btn.setObjectName("az_offset_onedn_btn")
        self.gridLayout_7.addWidget(self.az_offset_onedn_btn, 7, 8, 1, 1)
        self.az_offset_hundredup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_hundredup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_hundredup_btn.setObjectName("az_offset_hundredup_btn")
        self.gridLayout_7.addWidget(self.az_offset_hundredup_btn, 5, 6, 1, 1)
        self.az_offset_hundreddn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_hundreddn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_hundreddn_btn.setObjectName("az_offset_hundreddn_btn")
        self.gridLayout_7.addWidget(self.az_offset_hundreddn_btn, 7, 6, 1, 1)
        self.az_offset_tenthup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_tenthup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_tenthup_btn.setObjectName("az_offset_tenthup_btn")
        self.gridLayout_7.addWidget(self.az_offset_tenthup_btn, 5, 9, 1, 1)
        self.el_offset_tenup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.el_offset_tenup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.el_offset_tenup_btn.setObjectName("el_offset_tenup_btn")
        self.gridLayout_7.addWidget(self.el_offset_tenup_btn, 5, 12, 1, 1)
        self.el_offset_oneup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.el_offset_oneup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.el_offset_oneup_btn.setObjectName("el_offset_oneup_btn")
        self.gridLayout_7.addWidget(self.el_offset_oneup_btn, 5, 13, 1, 1)
        self.el_offset_onedn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.el_offset_onedn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.el_offset_onedn_btn.setObjectName("el_offset_onedn_btn")
        self.gridLayout_7.addWidget(self.el_offset_onedn_btn, 7, 13, 1, 1)
        self.el_offset_tenthdn_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.el_offset_tenthdn_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.el_offset_tenthdn_btn.setObjectName("el_offset_tenthdn_btn")
        self.gridLayout_7.addWidget(self.el_offset_tenthdn_btn, 7, 14, 1, 1)
        self.coord_viewer_el_label = QtWidgets.QLabel(self.coordinate_viewer)
        self.coord_viewer_el_label.setFrameShape(QtWidgets.QFrame.Box)
        self.coord_viewer_el_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.coord_viewer_el_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.coord_viewer_el_label.setObjectName("coord_viewer_el_label")
        self.gridLayout_7.addWidget(self.coord_viewer_el_label, 0, 11, 1, 5)
        self.az_offset_tenup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_tenup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_tenup_btn.setObjectName("az_offset_tenup_btn")
        self.gridLayout_7.addWidget(self.az_offset_tenup_btn, 5, 7, 1, 1)
        self.az_offset_oneup_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.az_offset_oneup_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.az_offset_oneup_btn.setObjectName("az_offset_oneup_btn")
        self.gridLayout_7.addWidget(self.az_offset_oneup_btn, 5, 8, 1, 1)
        self.auto_offset_reset_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.auto_offset_reset_btn.setGeometry(QtCore.QRect(25, 147, 90, 21))
        self.auto_offset_reset_btn.setObjectName("auto_offset_reset_btn")
        self.raw_tgt_reset_btn = QtWidgets.QPushButton(self.coordinate_viewer)
        self.raw_tgt_reset_btn.setGeometry(QtCore.QRect(25, 87, 90, 21))
        self.raw_tgt_reset_btn.setObjectName("raw_tgt_reset_btn")
        self.gridLayout_6.addWidget(self.coordinate_viewer, 1, 1, 10, 1)
        self.gs_connected_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.gs_connected_label.setFont(font)
        self.gs_connected_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gs_connected_label.setObjectName("gs_connected_label")
        self.gridLayout_6.addWidget(self.gs_connected_label, 0, 1, 1, 1)
        self.unwind = QtWidgets.QGroupBox(self.centralwidget)
        self.unwind.setObjectName("unwind")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.unwind)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.unwind_ccw_btn = QtWidgets.QPushButton(self.unwind)
        self.unwind_ccw_btn.setObjectName("unwind_ccw_btn")
        self.gridLayout_4.addWidget(self.unwind_ccw_btn, 0, 0, 1, 1)
        self.unwind_cw_btn = QtWidgets.QPushButton(self.unwind)
        self.unwind_cw_btn.setObjectName("unwind_cw_btn")
        self.gridLayout_4.addWidget(self.unwind_cw_btn, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.unwind_stop_btn = QtWidgets.QPushButton(self.unwind)
        self.unwind_stop_btn.setObjectName("unwind_stop_btn")
        self.gridLayout_8.addWidget(self.unwind_stop_btn, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.unwind, 4, 2, 2, 1)
        self.position_override = QtWidgets.QGroupBox(self.centralwidget)
        self.position_override.setObjectName("position_override")
        self.gridLayoutWidget = QtWidgets.QWidget(self.position_override)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 231, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.override_az_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.override_az_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.override_az_label.setObjectName("override_az_label")
        self.gridLayout_3.addWidget(self.override_az_label, 0, 0, 1, 1)
        self.override_az_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.override_az_btn.setObjectName("override_az_btn")
        self.gridLayout_3.addWidget(self.override_az_btn, 0, 2, 1, 1)
        self.override_az_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.override_az_input.setObjectName("override_az_input")
        self.gridLayout_3.addWidget(self.override_az_input, 0, 1, 1, 1)
        self.override_el_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.override_el_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.override_el_label.setObjectName("override_el_label")
        self.gridLayout_3.addWidget(self.override_el_label, 1, 0, 1, 1)
        self.override_el_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.override_el_input.setObjectName("override_el_input")
        self.gridLayout_3.addWidget(self.override_el_input, 1, 1, 1, 1)
        self.override_el_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.override_el_btn.setObjectName("override_el_btn")
        self.gridLayout_3.addWidget(self.override_el_btn, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.position_override, 4, 0, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NeedleGUI"))
        self.connections.setTitle(_translate("MainWindow", "Connections"))
        self.gpredict_port_label.setText(_translate("MainWindow", "Gpredict Port"))
        self.gstate_label.setText(_translate("MainWindow", "Gpredict State:"))
        self.serial_label.setText(_translate("MainWindow", "Serial State:"))
        self.gpredict_state_str.setText(_translate("MainWindow", "Disconnected"))
        self.serial_port_label.setText(_translate("MainWindow", "Serial Port"))
        self.serial_state_str.setText(_translate("MainWindow", "Disconnected"))
        self.gpredict_connect_btn.setText(_translate("MainWindow", "Open Gpredict Connection"))
        self.serial_connect_btn.setText(_translate("MainWindow", "Open Serial Connection"))
        self.spiral_search.setTitle(_translate("MainWindow", "Spiral Search Tool"))
        self.resolution_label.setText(_translate("MainWindow", "Resolution"))
        self.resolution_input.setText(_translate("MainWindow", "1"))
        self.speed_input.setText(_translate("MainWindow", "1"))
        self.speed_label.setText(_translate("MainWindow", "Speed"))
        self.search_button.setText(_translate("MainWindow", "Start Search"))
        self.searching_label.setText(_translate("MainWindow", "SPIRAL SEARCHING"))
        self.motor_state.setTitle(_translate("MainWindow", "Motor State"))
        self.enabled_state_el_btn.setText(_translate("MainWindow", "Disable EL"))
        self.enabled_state_az_btn.setText(_translate("MainWindow", "Disable AZ"))
        self.enabled_state_az_label.setText(_translate("MainWindow", "Azimuth Enabled"))
        self.enabled_state_el_label.setText(_translate("MainWindow", "Eleveation Enabled"))
        self.emergency_stop_btn.setText(_translate("MainWindow", "EMERGENCY STOP"))
        self.coordinate_viewer.setTitle(_translate("MainWindow", "Coordinate Viewer"))
        self.coord_viewer_az_label.setText(_translate("MainWindow", "AZIMUTH"))
        self.el_offset_tendn_btn.setText(_translate("MainWindow", "↓"))
        self.manual_offset_label.setText(_translate("MainWindow", "MANUAL OFFSET:"))
        self.manual_offset_az_minus.setText(_translate("MainWindow", "-"))
        self.manual_offset_az_label.setText(_translate("MainWindow", "000.0"))
        self.manual_offset_el_minus.setText(_translate("MainWindow", "-"))
        self.manual_offset_el_label.setText(_translate("MainWindow", "00.0"))
        self.raw_pos_label.setText(_translate("MainWindow", "RAW POSITION:"))
        self.raw_pos_az_label.setText(_translate("MainWindow", "000.0"))
        self.raw_pos_el_label.setText(_translate("MainWindow", "00.0"))
        self.sent_tgt_label.setText(_translate("MainWindow", "SENT TARGET:"))
        self.sent_tgt_az_label.setText(_translate("MainWindow", "000.0"))
        self.sent_tgt_el_label.setText(_translate("MainWindow", "00.0"))
        self.auto_offset_label.setText(_translate("MainWindow", "AUTOMATIC OFFSET:"))
        self.auto_offset_az_minus.setText(_translate("MainWindow", "-"))
        self.auto_offset_az_label.setText(_translate("MainWindow", "000.0"))
        self.auto_offset_el_minus.setText(_translate("MainWindow", "-"))
        self.auto_offset_el_label.setText(_translate("MainWindow", "00.0"))
        self.raw_tgt_label.setText(_translate("MainWindow", "RAW TARGET:"))
        self.raw_tgt_az_label.setText(_translate("MainWindow", "000.0"))
        self.raw_tgt_el_label.setText(_translate("MainWindow", "00.0"))
        self.az_offset_tenthdn_btn.setText(_translate("MainWindow", "↓"))
        self.el_offset_tenthup_btn.setText(_translate("MainWindow", "↑"))
        self.az_offset_tendn_btn.setText(_translate("MainWindow", "↓"))
        self.az_offset_onedn_btn.setText(_translate("MainWindow", "↓"))
        self.az_offset_hundredup_btn.setText(_translate("MainWindow", "↑"))
        self.az_offset_hundreddn_btn.setText(_translate("MainWindow", "↓"))
        self.az_offset_tenthup_btn.setText(_translate("MainWindow", "↑"))
        self.el_offset_tenup_btn.setText(_translate("MainWindow", "↑"))
        self.el_offset_oneup_btn.setText(_translate("MainWindow", "↑"))
        self.el_offset_onedn_btn.setText(_translate("MainWindow", "↓"))
        self.el_offset_tenthdn_btn.setText(_translate("MainWindow", "↓"))
        self.coord_viewer_el_label.setText(_translate("MainWindow", "ELEVATION"))
        self.az_offset_tenup_btn.setText(_translate("MainWindow", "↑"))
        self.az_offset_oneup_btn.setText(_translate("MainWindow", "↑"))
        self.auto_offset_reset_btn.setText(_translate("MainWindow", "RESET"))
        self.raw_tgt_reset_btn.setText(_translate("MainWindow", "RESET"))
        self.gs_connected_label.setText(_translate("MainWindow", "GS CONTROLLER NOT CONNECTED"))
        self.unwind.setTitle(_translate("MainWindow", "Unwind Tool"))
        self.unwind_ccw_btn.setText(_translate("MainWindow", "CCW Unwind"))
        self.unwind_cw_btn.setText(_translate("MainWindow", "CW Unwind"))
        self.unwind_stop_btn.setText(_translate("MainWindow", "STOP"))
        self.position_override.setToolTip(_translate("MainWindow", "Click \"Override\" to set the onboard position to the value in the input box"))
        self.position_override.setTitle(_translate("MainWindow", "Position Override"))
        self.override_az_label.setText(_translate("MainWindow", "Azimuth:"))
        self.override_az_btn.setText(_translate("MainWindow", "Override"))
        self.override_az_input.setText(_translate("MainWindow", "0"))
        self.override_el_label.setText(_translate("MainWindow", "Elevation:"))
        self.override_el_input.setText(_translate("MainWindow", "0"))
        self.override_el_btn.setText(_translate("MainWindow", "Override"))
