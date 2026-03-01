import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize,pyqtSignal
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout,QTabBar,QColorDialog)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup
import os
from modules.logic.export.skeleton_key_report import export_to_pdf
class SkeletonKeyHistoryUI(QWidget):
    def __init__(self,current_user):
        super().__init__()
        self.init_ui()
        self.current_user = current_user

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setObjectName("skeleton_key_history_ui")

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.upper_groupbox = QGroupBox("INFO")
        self.upper_groupbox_layout = QHBoxLayout()
        self.upper_groupbox.setLayout(self.upper_groupbox_layout)
        self.layout.addWidget(self.upper_groupbox,1)

        self.upper_groupbox_layout.addWidget(QLabel("DB ID"))

        self.db_id = QLineEdit()
        self.db_id.setReadOnly(True)
        self.upper_groupbox_layout.addWidget(self.db_id)

        self.upper_groupbox_layout.addStretch()

        self.upper_groupbox_layout.addWidget(QLabel("Date"))

        self.date = QLineEdit()
        self.date.setReadOnly(True)
        self.upper_groupbox_layout.addWidget(self.date)

        self.upper_groupbox_layout.addStretch()

        self.upper_groupbox_layout.addWidget(QLabel("Mode:"))

        self.mode = QLineEdit()
        self.mode.setReadOnly(True)
        self.upper_groupbox_layout.addWidget(self.mode)

        self.upper_groupbox_layout.addStretch()

        self.upper_groupbox_layout.addWidget(QLabel("Algorithm:"))

        self.algorithm = QLineEdit()
        self.algorithm.setReadOnly(True)
        self.upper_groupbox_layout.addWidget(self.algorithm)

        self.upper_groupbox_layout.addStretch()

        self.upper_groupbox_layout.addWidget(QLabel("Key:"))
        
        self.key = QLineEdit()
        self.key.setReadOnly(True)
        self.upper_groupbox_layout.addWidget(self.key)

        self.upper_groupbox_layout.addStretch()

        self.export_button = QPushButton("EXPORT")
        self.export_button.setMinimumWidth(200)
        self.export_button.clicked.connect(self.export_button_function)
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

    def export_button_function(self):

        default_name = f"SkeletonKey_Audit_{self.db_id.text()}.pdf"
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Audit Report", default_name, "PDF Files (*.pdf)")
        if file_path:
            try:
                export_to_pdf(       
                            file_path,
                            self.db_id.text().strip(),
                            self.date.text().strip(),
                            self.mode.text().strip(),
                            self.algorithm.text().strip(),
                            self.key.text().strip(),
                            self.input_text.toPlainText().strip(),
                            self.output_text.toPlainText().strip()
                                            )
            except Exception as e:
                print(str(e))

