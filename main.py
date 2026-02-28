import sys
import subprocess
from PyQt6.QtWidgets import QApplication
from modules.ui.main_ui import MainUI
from modules.ui.login_ui import LoginUI
from modules.ui.skeleton_key_ui import SkeletonKeyUI
from modules.logic.login.database_manager import DatabaseManager


class AppManager():
    def __init__(self):
        self.app = QApplication(sys.argv) 
        self.start_docker_db()               
        self.main_ui = MainUI()
        self.database_manager = DatabaseManager()
        self.login_ui = LoginUI()
        self.login_ui.login_inputs.connect(self.handle_login)
        
    def init_main_ui(self):
        self.main_ui.central_wiget.addTab(self.login_ui,"Login")
        self.main_ui.showMaximized()
        sys.exit(self.app.exec())

    def handle_login(self,login_inputs):
        username = login_inputs[0]
        password = login_inputs[1]
        login_code = self.database_manager.check_login(username,password)
        if login_code == 0:
            self.login_ui.error_space.setText("Invalid Username or Password")
        else:
            self.main_ui.central_wiget.removeTab(0)
            self.skeleton_key_ui = SkeletonKeyUI(self.database_manager,username)
            self.main_ui.central_wiget.addTab(self.skeleton_key_ui,"Skeleton Key")

    def start_docker_db(self):
        try:
            subprocess.run(["docker-compose","up","-d"],check=True)

        except FileNotFoundError:
            print("Error : Docker is not found")

        except subprocess.CalledProcessError as e:
            print(f"Error : {e}")

if __name__ == "__main__":
    manager = AppManager()
    manager.init_main_ui()