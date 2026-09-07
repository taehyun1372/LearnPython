from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt6.QtCore import pyqtSignal, QObject
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        central = QWidget()

        start_button = QPushButton("start")
        stop_button = QPushButton("stop")
        
        self._gui_objects = {}
        self._gui_objects["start_button"] = start_button
        self._gui_objects["stop_button"] = stop_button
        
        layout.addWidget(start_button, 0)
        layout.addWidget(stop_button, 1)

        central.setLayout(layout)
        self.setCentralWidget(central)
    
    @property
    def gui_objects(self):
        return self._gui_objects
    
class GUIInf(QObject):
    update_pushbutton_signal = pyqtSignal(QPushButton, list)
    
    def __init__(self):
        super().__init__()
        self.update_pushbutton_signal.connect(self.update_pushbutton_command)
    
    def emit_update_pushbutton_signal(self, push_button: QPushButton, list: list):
        self.update_pushbutton_signal.emit(push_button, list)
        
    def update_pushbutton_command(self, push_button: QPushButton, list):
        if push_button:
            push_button.clicked.connect(list[0])
    
class Presenter:
    def __init__(self, gui_objects):
        self._gui_inf = GUIInf()
        self._gui_objects = gui_objects
        self.initialize()
    
    def initialize(self):
        self._gui_inf.emit_update_pushbutton_signal(self._gui_objects.get("start_button", None), [self.start_process])
        self._gui_inf.emit_update_pushbutton_signal(self._gui_objects.get("stop_button", None), [self.stop_process])
    
    def start_process(self):
        print("process started..")
        
    def stop_process(self):
        print("process stopped..")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyMainWindow()
    
    presenter = Presenter(main.gui_objects)

    main.show()
    app.exec()