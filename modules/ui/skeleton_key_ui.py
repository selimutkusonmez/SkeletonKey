import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize,pyqtSignal,QDate,QTime
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout,QTabBar,QColorDialog,QDateEdit,QListWidgetItem)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup
import os

from modules.ui.skeleton_key_history_ui import SkeletonKeyHistoryUI

class SkeletonKeyUI(QWidget):
    def __init__(self,DatabaseManager,MainUI,CurrentUser):
        super().__init__()
        self.database_manager = DatabaseManager
        self.current_user = CurrentUser
        self.main_ui = MainUI
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
        self.algorithm_items()
        self.left_group_box_layout.addWidget(self.algorithm_input, 2, 1)

        self.left_group_box_layout.addWidget(QLabel("Mode:"), 3, 0)

        self.mode_input = QComboBox()
        self.mode_input.addItems(["🔒 Encrypt", "🔓 Decrypt"])
        self.left_group_box_layout.addWidget(self.mode_input, 3, 1)

        self.run_process_button = QPushButton("RUN PROCESS")
        self.run_process_button.clicked.connect(self.run_process_button_func)
        self.left_group_box_layout.addWidget(self.run_process_button, 4, 0, 1, 2)

        self.error_space = QLineEdit()
        self.error_space.setObjectName("error_space")
        self.left_group_box_layout.addWidget(self.error_space,5,0,1,2)
        self.left_group_box_layout.setRowStretch(6, 1)

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
        self.history_start_date_picker.setDate(today.addDays(-7))
        self.history_start_date_picker.setCalendarPopup(True)
        self.history_start_date_picker.setMaximumDate(today)
        self.right_group_box_layout.addWidget(self.history_start_date_picker,0,1)

        self.right_group_box_layout.addWidget(QLabel("End : "),1,0)
        self.history_end_date_picker = QDateEdit()
        self.history_end_date_picker.setDate(QDate.currentDate())
        self.history_end_date_picker.setCalendarPopup(True)
        self.history_end_date_picker.setMaximumDate(today)
        self.right_group_box_layout.addWidget(self.history_end_date_picker,1,1)

        self.history_button = QPushButton("Bring History")
        self.history_button.clicked.connect(self.bring_history_button_func)
        self.right_group_box_layout.addWidget(self.history_button,2,0,1,2)

        self.history_list = QListWidget()
        self.history_list.itemDoubleClicked.connect(self.history_list_item_doubleclicked)
        self.right_group_box_layout.addWidget(self.history_list,3,0,1,2)

        self.refresh_button = QPushButton("Refresh History")
        self.refresh_button.clicked.connect(self.refresh_button_func)
        self.right_group_box_layout.addWidget(self.refresh_button,4,0)

        self.clear_history_button = QPushButton("Clear History")
        self.clear_history_button.clicked.connect(self.clear_history_button_func)
        self.right_group_box_layout.addWidget(self.clear_history_button,4,1)

        self.left_hide = False
        self.right_hide = False
        self.current_session_history = []

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
        try:
            key = self.key_input.text() if self.key_input.text() != "" else None
            algorithm = self.algorithm_input.currentText() if not self.algorithm_input.currentText().startswith("---") else None
            mode = self.mode_input.currentText()
            input_text = self.input_text.toPlainText() if self.input_text.toPlainText() != "" else None
            output_text = self.output_text.toPlainText()
            time = QTime.currentTime().toString("HH:mm")
            if None in [key,algorithm,mode,input_text,output_text,time]:
                self.error_space.setText("Please fill in all fields and select a valid algorithm to proceed.")
                return
            self.error_space.setText("")
            db_id = self.database_manager.make_history(self.current_user,mode,algorithm,key,input_text,output_text)

            if isinstance(db_id, str) and db_id.startswith("Error"):
                self.error_space.setText(db_id)
                return
            
            history_text = f"{db_id} | {time} | {mode} | {algorithm} | {key}"
            history_item = QListWidgetItem(history_text)
            history_item.setData(Qt.ItemDataRole.UserRole, db_id)
            
            self.history_list.addItem(history_item)
            self.current_session_history.append({"text": history_text, "id": db_id})

        except Exception as e:
            self.error_space.setText(f"Error: {str(e)}")

    def history_list_item_doubleclicked(self,item):
        try:
            db_id = item.data(Qt.ItemDataRole.UserRole)
            history_data = self.database_manager.show_clicked_history(db_id)

            if isinstance(history_data, str) and history_data.startswith("Error"):
                self.error_space.setText(history_data)
                return
            
            date = history_data[2].strftime("%Y-%m-%d %H:%M")
            self.skeleton_key_history_ui = SkeletonKeyHistoryUI()
            self.skeleton_key_history_ui.db_id.setText(str(history_data[0]))
            self.skeleton_key_history_ui.date.setText(date)
            self.skeleton_key_history_ui.mode.setText(str(history_data[3]))
            self.skeleton_key_history_ui.algorithm.setText(str(history_data[4]))
            self.skeleton_key_history_ui.key.setText(str(history_data[5]))
            self.skeleton_key_history_ui.input_text.setText(str(history_data[6]))
            self.skeleton_key_history_ui.output_text.setText(str(history_data[7]))

            index = self.main_ui.central_widget.addTab(self.skeleton_key_history_ui,f"{db_id}")
            self.main_ui.central_widget.setCurrentIndex(index)

        except Exception as e:
            self.error_space.setText(f"Error: {str(e)}")
        
    def refresh_button_func(self):
        self.history_list.clear()

        for data in self.current_session_history:
            item = QListWidgetItem(data["text"])
            item.setData(Qt.ItemDataRole.UserRole, data["id"])
            self.history_list.addItem(item)


    def clear_history_button_func(self):
        self.history_list.clear()

    def bring_history_button_func(self):
        try:
            self.history_list.clear()
            start_date = self.history_start_date_picker.date().toString()
            end_date = self.history_end_date_picker.date().toString()
            data = self.database_manager.show_history_by_date(self.current_user,start_date,end_date)

            if isinstance(data, str) and data.startswith("Error"):
                self.error_space.setText(data)
                return
            
            for row in data:
                date = row[2].strftime("%Y-%m-%d %H:%M")
                history_text = f"{row[0]} | {date} | {row[3]} | {row[4]} | {row[5]}"
                history_item = QListWidgetItem(history_text)
                history_item.setData(Qt.ItemDataRole.UserRole, row[0])
                self.history_list.addItem(history_item)

        except Exception as e:
            self.error_space.setText(f"Error: {str(e)}")

    def algorithm_items(self):
        headers = {
            "--- 📜 Historical & Classic Ciphers ---" : ["🗝️ Caesar","🗝️ Vigenère","🗝️ ROT13","🗝️ Atbash"],
            "--- ⚙️ Bitwise & Logic Ciphers ---" : ["⛓️ XOR"],
            "--- 🔐 Modern Symmetric Encryption ---" : ["🔒 AES-256","🔒 DES","🔒 Blowfish"],
            "--- 🔏 Asymmetric Cryptography ---" : ["🗝️ RSA"],
            "--- 🧮 Encoding & Hashing ---" : ["🧩 Base64","🏷️ SHA-256"]
                }

        for key,val in headers.items():
            self.algorithm_input.addItem(key)
            header_index = self.algorithm_input.count() - 1
            model = self.algorithm_input.model()
            item = model.item(header_index)
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEnabled)
            for i in val:
                self.algorithm_input.addItem(i)          


    
