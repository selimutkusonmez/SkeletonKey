import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize,pyqtSignal
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout,QTabBar,QColorDialog)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup
import os
from modules.logic.style_reader.style_reader import read_style
from config import JPG_PATH

class SkeletonKeyHistoryUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setObjectName("skeleton_key_history_ui")

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.upper_groupbox = QGroupBox("INFO")
        self.upper_groupbox_layout = QHBoxLayout()
        self.upper_groupbox.setLayout(self.upper_groupbox_layout)
        self.layout.addWidget(self.upper_groupbox,1)

        self.upper_groupbox_layout.addWidget(QLabel("Key:"))
        
        self.key_input = QLineEdit()
        self.key_input.setReadOnly(True)
        self.upper_groupbox_layout.addWidget(self.key_input)

        self.upper_groupbox_layout.addStretch()
        
        self.upper_groupbox_layout.addWidget(QLabel("Algorithm:"))

        self.algorithm_input = QComboBox()
        self.algorithm_input.setMinimumWidth(150)
        self.upper_groupbox_layout.addWidget(self.algorithm_input)

        self.upper_groupbox_layout.addStretch()

        self.upper_groupbox_layout.addWidget(QLabel("Mode:"))

        self.type_input = QComboBox()
        self.type_input.setMinimumWidth(150)
        self.type_input.addItems(["Encrypt", "Decrypt"])
        self.upper_groupbox_layout.addWidget(self.type_input)

        self.upper_groupbox_layout.addStretch()

        self.export_button = QPushButton("EXPORT")
        self.export_button.setMinimumWidth(200)
        self.upper_groupbox_layout.addWidget(self.export_button)

        self.middle_groupbox = QGroupBox("INPUT")
        self.middle_groupbox_layout = QVBoxLayout()
        self.middle_groupbox.setLayout(self.middle_groupbox_layout)
        self.layout.addWidget(self.middle_groupbox,3)

        self.input_text = QTextEdit()
        self.input_text.setReadOnly(True)
        self.middle_groupbox_layout.addWidget(self.input_text)

        self.bottom_groupbox = QGroupBox("OUTPUT")
        self.bottom_groupbox_layout = QVBoxLayout()
        self.bottom_groupbox.setLayout(self.bottom_groupbox_layout)
        self.layout.addWidget(self.bottom_groupbox,3)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.bottom_groupbox_layout.addWidget(self.output_text)

