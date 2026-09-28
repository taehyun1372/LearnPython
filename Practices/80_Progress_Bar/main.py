from enum import Enum
import traceback
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QProgressBar, QPushButton
from PyQt6.QtCore import QObject, pyqtSignal
import sys
import threading
import time

class MyMainWindow(QMainWindow):
    start_clicked = pyqtSignal()
    stop_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        central = QWidget()
        layout = QGridLayout()
        
        self.description = QLabel("Progress bar")
        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setStyleSheet("""
            QProgressBar {
            border: none;
            border-radius: 6px;
            text-align: center;
            background-color: #E5E7EB;
            color: black;
            height: 20px;
            }
            
            QProgressBar::chunk {
            border-radius: 6px;
            background-color: #3B82F6;
            }
            """)
        
        self.btn_start = QPushButton("Start")
        self.btn_stop = QPushButton("Stop")
        self.btn_error = QPushButton("Error")
        self.btn_start.clicked.connect(self.start_button_pressed)
        self.btn_stop.clicked.connect(self.stop_button_pressed)
        self.btn_error.clicked.connect(self.error_button_pressed)
        
        self.status = QLabel("")
        
        layout.addWidget(self.description, 0, 0)
        layout.addWidget(self.progress, 0, 1)
        
        layout.addWidget(self.btn_start, 1, 0)
        layout.addWidget(self.btn_stop, 1, 1)
        layout.addWidget(self.status, 1, 2)
        layout.addWidget(self.btn_error, 2, 0)
        
        central.setLayout(layout)
        self.setCentralWidget(central)
        
    def start_button_pressed(self):
        self.start_clicked.emit()
        
    def stop_button_pressed(self):
        self.stop_clicked.emit()
    
    def error_button_pressed(self):
        raise ValueError("Error button clicked!")
        
    def increase(self):
        value = self.progress.value()
        self.progress.setValue(min(100, value + 10))
        
    def decrease(self):
        value = self.progress.value()
        self.progress.setValue(max(0, value - 10))
        
class TestSteps():
    def __init__(self):
        pass
    
    def step1(self):
        self.step_start_info("step 1")
        time.sleep(2)
        self.step_end_info("step 1")
        
    def step2(self):
        self.step_start_info("step 2")
        time.sleep(2)
        self.step_end_info("step 2")
        
    def step3(self):
        self.step_start_info("step 3")
        time.sleep(2)
        self.step_end_info("step 3")
        
    def step4(self):
        self.step_start_info("step 4")
        time.sleep(2)
        self.step_end_info("step 4")
        
    def step_start_info(self, step_name):
        print(f"----------{step_name} started----------")
    
    def step_end_info(self, step_name):
        print(f"----------{step_name} finished----------")

class Status(Enum):
    IDLE = 0
    READY = 1
    RUNNING = 2
    STOPPING = 3

class TestHandler(QObject):
    progress_update_signal = pyqtSignal(int)
    status_changed_signal = pyqtSignal(Status)
    error_signal = pyqtSignal(str)
    
    def __init__(self, test_steps: TestSteps, receipe = None):
        super().__init__()
        self.status_changed_signal.emit(Status.IDLE)
        self.test_steps = test_steps
        self.receipe = receipe
        self.is_stop_event_set = threading.Event()
        self.is_start_event_set = threading.Event()
        self.handler_thread = None
        self.test_runner_thread = None
    
    def initialize(self):
        if self.handler_thread:
            return
        self.handler_thread = threading.Thread(target=self.__test_handler, daemon=True)
        self.handler_thread.start()
        self.status_changed_signal.emit(Status.READY)
    
    def __test_handler(self):
        while True:
            time.sleep(0.1) 
            # Starting logic
            if self.is_start_event_set.is_set():
                self.__start_test()
                self.is_start_event_set.clear()
            # Stopping logic
            elif self.is_stop_event_set.is_set():
                self.__stop_test()
                self.is_stop_event_set.clear()
            
    def start_test(self):
        self.is_start_event_set.set()
    
    def __start_test(self):
        if self.test_runner_thread and self.test_runner_thread.is_alive():
            return
        self.test_runner_thread = threading.Thread(target=self.__process_test, daemon=True)
        self.test_runner_thread.start()
        self.status_changed_signal.emit(Status.RUNNING)
        
    def __process_test(self):
        try:
            if self.receipe is None:
                raise AttributeError(f"Recipe is missing!")
            total_count = len(self.receipe)
            progress_count = 0
            self.progress_update_signal.emit(0)
            for k, v in self.receipe.items():
                if self.is_stop_event_set.is_set():
                    break
                step_cmd = getattr(self.test_steps, v, None)
                if not step_cmd :
                    raise AttributeError("Cannot find step definition!")
                step_cmd()
                progress_count+=1
                progress_rate = int(progress_count / total_count * 100)
                self.progress_update_signal.emit(progress_rate)
        except Exception:
            self.error_signal.emit(traceback.format_exc())
        finally:
            self.status_changed_signal.emit(Status.READY)
            
    def stop_test(self):
        self.is_stop_event_set.set()
        self.status_changed_signal.emit(Status.STOPPING)
    
    def __stop_test(self):
        if self.test_runner_thread and self.test_runner_thread.is_alive():
            self.test_runner_thread.join()
        self.status_changed_signal.emit(Status.READY)
    
    def set_recipe(self, receipe):
        self.receipe = receipe

class Presenter(QObject):
    def __init__(self, main_window: MyMainWindow, test_handler: TestHandler):
        super().__init__()
        self.main_window = main_window
        self.test_handler = test_handler
        self.test_handler.progress_update_signal.connect(self.__progress_update)
        self.test_handler.status_changed_signal.connect(self.__status_update)
        self.test_handler.error_signal.connect(self.__error_update)
        self.main_window.start_clicked.connect(self.__start_test)
        self.main_window.stop_clicked.connect(self.__stop_test)
        
    def __progress_update(self, progress_rate):
        progress_widget = getattr(self.main_window, "progress")
        if progress_widget:
            progress_widget.setValue(progress_rate)
            
    def __status_update(self, status: Status):
        status_widget = getattr(self.main_window, "status")
        if status_widget:
            status_widget.setText(str(status))
            
    def __start_test(self):
        if self.test_handler:
            self.test_handler.start_test()
    
    def __stop_test(self):
        if self.test_handler:
            self.test_handler.stop_test()
            
    def __error_update(self, error_message):
        if self.main_window:
            QMessageBox.critical(
                self.main_window,
                "Application Error",
                error_message,
            )

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        main = MyMainWindow()
        
        test_steps = TestSteps()
        test_handler = TestHandler(test_steps)
        test_receipe = {
            1 : "step1",
            2 : "step2",
            3 : "step3",
            4 : "step4",
            5 : "step5"
        }
        presenter = Presenter(main, test_handler)
        test_handler.initialize()
        test_handler.set_recipe(test_receipe)

        main.show()
        app.exec()
    except Exception:
        print(traceback.format_exc())
