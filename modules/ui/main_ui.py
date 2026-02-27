import sys
import subprocess
from PyQt6.QtCore import Qt,QRegularExpression,QSize
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QStatusBar,QSizePolicy,QHBoxLayout,QTabBar,QColorDialog)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter,QFontDatabase,QFont,QAction,QActionGroup
import os
from modules.logic.style_reader.style_reader import read_style
from config import JPG_PATH

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.current_theme = "dark"
        self.current_font_size = 30
        self.current_font_color = "#ADBAC7"
        self.dark_theme_action_function()
        

    def init_ui(self):

        self.central_wiget = QTabWidget()
        self.setCentralWidget(self.central_wiget)

        self.setContentsMargins(0,0,0,0)
        #StatusBar
        self.setStatusBar(QStatusBar())

        #MenuBar created
        menu_bar = self.menuBar()

        #File Menu
        file_menu = menu_bar.addMenu("File")
        restart_app_action = QAction("Restart App",self)
        restart_app_action.setShortcut("Ctrl+R")
        restart_app_action.triggered.connect(self.restart_app_action_function)
        file_menu.addAction(restart_app_action)

        about_action = QAction("About",self)
        about_action.triggered.connect(self.about_action_function)
        file_menu.addAction(about_action)

        #Settings Menu
        settings_menu = menu_bar.addMenu("Settings")

        theme_menu = settings_menu.addMenu("Theme")
        theme_action_group = QActionGroup(self)

        font_menu = settings_menu.addMenu("Font Size")
        font_action_group = QActionGroup(self)

        color_menu = settings_menu.addMenu("Font Color")
        color_action_group = QActionGroup(self)

        #Light Theme
        light_theme_action = QAction("Light Theme")
        light_theme_action.setShortcut("Ctrl+L")
        light_theme_action.setCheckable(True)
        theme_menu.addAction(light_theme_action)
        theme_action_group.addAction(light_theme_action)
        light_theme_action.triggered.connect(self.light_theme_action_function)

        #Dark Theme
        dark_theme_action = QAction("Dark Theme")
        dark_theme_action.setShortcut("Ctrl+D")
        dark_theme_action.setCheckable(True)
        dark_theme_action.setChecked(True)
        theme_menu.addAction(dark_theme_action)
        theme_action_group.addAction(dark_theme_action)
        dark_theme_action.triggered.connect(self.dark_theme_action_function)

        #Increase Font Size
        increase_font_size_action = QAction("Increase Font Size")
        increase_font_size_action.setShortcut("Ctrl++")
        font_menu.addAction(increase_font_size_action)
        font_action_group.addAction(increase_font_size_action)
        increase_font_size_action.triggered.connect(self.increase_font_size_action_function)

        #Decrease Font Size
        decrease_font_size_action = QAction("Decrease Font Size")
        decrease_font_size_action.setShortcut("Ctrl+-")
        font_menu.addAction(decrease_font_size_action)
        font_action_group.addAction(decrease_font_size_action)
        decrease_font_size_action.triggered.connect(self.decrease_font_size_action_function)

        #Font Color
        change_color_action = QAction("Change Font Color")
        color_menu.addAction(change_color_action)
        color_action_group.addAction(change_color_action)
        change_color_action.triggered.connect(self.change_color_action_function)

    def restart_app_action_function(self):
        QApplication.quit()
        subprocess.Popen([sys.executable, *sys.argv])

    def light_theme_action_function(self):
        self.current_theme = "light"
        if self.current_font_color == "#ADBAC7":
            self.current_font_color = "#24292F"
        self.setStyleSheet(read_style(self.current_theme,self.current_font_size,self.current_font_color))

    def dark_theme_action_function(self):
        self.current_theme = "dark"
        if self.current_font_color =="#24292F" :
            self.current_font_color = "#ADBAC7"
        self.setStyleSheet(read_style(self.current_theme,self.current_font_size,self.current_font_color))
        
    def chosen_subject(self,chosen_subject):
        self.statusBar().showMessage(chosen_subject)

    def about_action_function(self):
        about_text = """
        <h2>Statistical Calculator v1.0</h2>
        <p>A comprehensive and interactive statistical analysis tool designed to simplify complex calculations. From basic descriptive statistics to advanced hypothesis testing, this application provides accurate results alongside real-time dynamic formula rendering.</p>
        <p><b>Developer:</b> Selim Utku Sönmez, Computer Engineering Student<br>
        <b>Powered by:</b> Python, PyQt6</p>
        """
        QMessageBox.about(self, "About Statistical Calculator", about_text)
    
    def increase_font_size_action_function(self):
        if 25 <= self.current_font_size < 60:
            self.current_font_size += 1
        else:
            return
        self.setStyleSheet(read_style(self.current_theme,self.current_font_size,self.current_font_color))

    def decrease_font_size_action_function(self):
        if 25 < self.current_font_size <= 60:
            self.current_font_size -= 1
        else:
            return
        self.setStyleSheet(read_style(self.current_theme,self.current_font_size,self.current_font_color))

    def change_color_action_function(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.current_font_color = color.name()
            self.setStyleSheet(read_style(self.current_theme,self.current_font_size,self.current_font_color))
        else:
            return

    

