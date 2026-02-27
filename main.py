import sys
from PyQt6.QtWidgets import QApplication

from modules.ui.main_ui import MainUI
from modules.ui.login_ui import LoginUI
from modules.ui.skeleton_key_ui import SkeletonKeyUI
from modules.ui.skeleton_key_history_ui import SkeletonKeyHistoryUI

class AppManager():
    def __init__(self):
        self.app = QApplication(sys.argv)                
        self.main_ui = MainUI()
        self.login_ui = LoginUI()
        self.skeleton_key_ui = SkeletonKeyUI()
        self.skeleton_key_history_ui = SkeletonKeyHistoryUI()

        self.login_ui.login_status_code.connect(self.handle_login)
        
    def init_main_ui(self):
        self.main_ui.central_wiget.addTab(self.login_ui,"Login")
        self.main_ui.central_wiget.addTab(self.skeleton_key_ui,"Skeleton Key")
        self.main_ui.central_wiget.addTab(self.skeleton_key_history_ui,"Skeleton History Key")
        self.main_ui.showMaximized()
        sys.exit(self.app.exec())

    def handle_login(self,login_status_code):
        if login_status_code == 0:
            print("sa")

if __name__ == "__main__":
    manager = AppManager()
    manager.init_main_ui()