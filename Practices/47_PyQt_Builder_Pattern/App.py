import sys
import os
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import json

class Config:
    def __init__(self, conf_name: str):
        self.data = None
        base_dir = os.path.dirname(os.path.abspath(__file__))
        conf_path = os.path.join(base_dir, "App.json")
        with open(conf_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)[conf_name]
            
    def get_ui_file_name(self):
        return self.data["ui_file"]
    
    def get_test_file_name(self):
        return self.data["test_file"]
        
class WinFactory:
    def __init__(self, config: Config):
        self.config = config
    
    def build_application(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_name = self.config.get_ui_file_name()
        test_file_name = self.config.get_test_file_name()
        
        ui_file_path = os.path.join(base_dir, ui_file_name)
        test_file_path = os.path.join(base_dir, test_file_name)
        
        return MainWindow(ui_file_path, test_file_path);
    
class MainWindow(QMainWindow):
    def __init__(self, ui_file_path, test_file_path):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        
        with open(test_file_path, "r", encoding="utf-8") as f:
            test_data = json.load(f)
        
        print(test_data)
        
        ui_file.close()
        self.setFixedSize(800, 600)
        self.setCentralWidget(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    arg = sys.argv[1]
    
    conf = Config(arg)
    factory = WinFactory(conf)
    
    win1 = factory.build_application()
    
    win1.show()
    app.exec()
    
    print("Something..")
    
