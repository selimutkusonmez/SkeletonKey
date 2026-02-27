import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize,pyqtSignal
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout,QTabBar,QColorDialog)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup
import os
from modules.logic.style_reader.style_reader import read_style
from config import JPG_PATH

class SkeletonKeyUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)
        self.setObjectName("skeleton_key_ui")

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.left_group_box = QGroupBox("Configuration")
        self.left_group_box_layout = QGridLayout()
        self.left_group_box.setLayout(self.left_group_box_layout)
        self.left_group_box.setMinimumWidth(250) 
        self.layout.addWidget(self.left_group_box)

        self.left_group_box_layout.setRowStretch(0,1)

        self.left_group_box_layout.addWidget(QLabel("Key:"), 1, 0)
        
        self.key_input = QLineEdit()
        self.left_group_box_layout.addWidget(self.key_input, 1, 1)

        
        self.left_group_box_layout.addWidget(QLabel("Algorithm:"), 2, 0)

        self.algorithm_input = QComboBox()
        self.left_group_box_layout.addWidget(self.algorithm_input, 2, 1)

        self.left_group_box_layout.addWidget(QLabel("Mode:"), 3, 0)

        self.type_input = QComboBox()
        self.type_input.addItems(["Encrypt", "Decrypt"])
        self.left_group_box_layout.addWidget(self.type_input, 3, 1)

        self.button = QPushButton("RUN PROCESS")
        self.left_group_box_layout.addWidget(self.button, 4, 0, 1, 2)
        self.left_group_box_layout.setRowStretch(5, 1)

        self.middle_group_box = QGroupBox("Editor")
        self.middle_group_box_layout = QVBoxLayout()
        self.middle_group_box.setLayout(self.middle_group_box_layout)
        self.layout.addWidget(self.middle_group_box,1)

        self.middle_group_box_layout.addWidget(QLabel("INPUT DATA"))

        self.input_text = QTextEdit()
        self.middle_group_box_layout.addWidget(self.input_text)

        self.bottom_group_box = QGroupBox()
        self.bottom_group_box.setObjectName("top_group_box")
        self.bottom_group_box_layout = QHBoxLayout()
        self.bottom_group_box.setLayout(self.bottom_group_box_layout)
        
        self.hide_left_button = QPushButton("Toggle Settings")
        self.hide_left_button.clicked.connect(self.hide_left_button_funtion)
        self.bottom_group_box_layout.addWidget(self.hide_left_button)
        
        self.bottom_group_box_layout.addStretch()

        self.hide_right_button = QPushButton("Toggle History")
        self.hide_right_button.clicked.connect(self.hide_right_button_function)
        self.bottom_group_box_layout.addWidget(self.hide_right_button)
        
        self.middle_group_box_layout.addWidget(self.bottom_group_box)

        self.middle_group_box_layout.addWidget(QLabel("OUTPUT RESULT"))
        
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.middle_group_box_layout.addWidget(self.output)

        self.right_group_box = QGroupBox("Activity History")
        self.right_group_box_layout = QVBoxLayout()
        self.right_group_box.setLayout(self.right_group_box_layout)
        self.layout.addWidget(self.right_group_box)
        self.right_group_box.setMinimumWidth(280)

        self.history_list = QListWidget()
        self.right_group_box_layout.addWidget(self.history_list)

        self.clear_history_button = QPushButton("Clear History")
        self.right_group_box_layout.addWidget(self.clear_history_button)



        self.left_hide = False
        self.right_hide = False

    def hide_left_button_funtion(self):
        if not self.left_hide:
            self.left_group_box.hide()
            self.left_hide = True
        else:
            self.left_group_box.show()
            self.left_hide = False

    def hide_right_button_function(self):
        if not self.right_hide:
            self.right_group_box.hide()
            self.right_hide = True
        else:
            self.right_group_box.show()
            self.right_hide = False