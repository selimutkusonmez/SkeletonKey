import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize,pyqtSignal,QDate
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout,QTabBar,QColorDialog,QDateEdit,QListWidgetItem)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup
import os

from modules.ui.skeleton_key_history_ui

class SkeletonKeyUI(QWidget):
    def __init__(self,DatabaseManager,CurrentUser):
        super().__init__()
        self.database_manager = DatabaseManager
        self.current_user = CurrentUser
        print(self.current_user)
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
        self.algorithm_input.addItems(["sa"])
        self.left_group_box_layout.addWidget(self.algorithm_input, 2, 1)

        self.left_group_box_layout.addWidget(QLabel("Mode:"), 3, 0)

        self.mode_input = QComboBox()
        self.mode_input.addItems(["Encrypt", "Decrypt"])
        self.left_group_box_layout.addWidget(self.mode_input, 3, 1)

        self.run_process_button = QPushButton("RUN PROCESS")
        self.run_process_button.clicked.connect(self.run_process_button_func)
        self.left_group_box_layout.addWidget(self.run_process_button, 4, 0, 1, 2)
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
        
        self.output_text = QTextEdit()

        self.middle_group_box_layout.addWidget(self.output_text)

        self.right_group_box = QGroupBox("Activity History")
        self.right_group_box_layout = QGridLayout()
        self.right_group_box.setLayout(self.right_group_box_layout)
        self.layout.addWidget(self.right_group_box)
        self.right_group_box.setMinimumWidth(280)

        today = QDate.currentDate()
        self.right_group_box_layout.addWidget(QLabel("Start : "),0,0)
        self.history_start_date_picker = QDateEdit()
        self.history_start_date_picker.setDate(QDate.currentDate())
        self.history_start_date_picker.setCalendarPopup(True)
        self.history_start_date_picker.setMaximumDate(today)
        self.history_start_date_picker.setMaximumDate(today.addDays(-7))
        self.right_group_box_layout.addWidget(self.history_start_date_picker,0,1)

        self.right_group_box_layout.addWidget(QLabel("End : "),1,0)
        self.history_end_date_picker = QDateEdit()
        self.history_end_date_picker.setDate(QDate.currentDate())
        self.history_end_date_picker.setCalendarPopup(True)
        self.history_end_date_picker.setMaximumDate(today)
        self.history_end_date_picker.setMaximumDate(today)
        self.right_group_box_layout.addWidget(self.history_end_date_picker,1,1)

        self.history_button = QPushButton("Bring History")
        self.right_group_box_layout.addWidget(self.history_button,2,0,1,2)

        self.history_list = QListWidget()
        self.history_list.itemDoubleClicked.connect(self.history_list_item_doubleclicked)
        self.right_group_box_layout.addWidget(self.history_list,3,0,1,2)

        self.refresh_button = QPushButton("Refresh History")
        self.right_group_box_layout.addWidget(self.refresh_button,4,0)

        self.clear_history_button = QPushButton("Clear History")
        self.right_group_box_layout.addWidget(self.clear_history_button,4,1)

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

    def run_process_button_func(self):
        key = self.key_input.text()
        algorithm = self.algorithm_input.currentText()
        mode = self.mode_input.currentText()
        input_text = self.input_text.toPlainText()
        output_text = self.output_text.toPlainText() 
        date = QDate.currentDate().toString("dd.MM.yyyy")
        history_text = f"{date} | {algorithm} | {mode} | {key}"
        history_item = QListWidgetItem(history_text)
        db_id = self.database_manager.make_history(self.current_user,mode,algorithm,key,input_text,output_text)
        history_item.setData(Qt.ItemDataRole.UserRole, db_id)
        self.history_list.addItem(history_item)

    def history_list_item_doubleclicked(self,item):
        db_id = item.data(Qt.ItemDataRole.UserRole)
        try:
            self.his