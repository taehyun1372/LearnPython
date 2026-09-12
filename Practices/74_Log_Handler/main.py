import time
from datetime import datetime
import enum
from pathlib import Path
import threading

class LogLevel(enum.IntEnum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ALARM = 3
    ERROR = 4

class LogHandler():
    def __init__(self, log_level: LogLevel, file_path: Path= None):
        self.log_level = log_level
        self._file_path = None
        if file_path:
            self.file_path = file_path
        self.lock = threading.Lock()
    
    @property
    def file_path(self) -> Path:
        return self._file_path
    
    @file_path.setter
    def file_path(self, path: Path):
        if not isinstance(path, Path):
            raise TypeError("path should Path type")
        self._file_path = path
    
    @property
    def log_level(self) -> LogLevel: 
        return self._log_level
    
    @log_level.setter
    def log_level(self, log_level: LogLevel):
        if not isinstance(log_level, LogLevel):
            raise TypeError("Log level should be LogLevel type")
        self._log_level = log_level
        
    def get_logger(self, instance):
        return Logger(self, type(instance).__name__)
    
    def log(self, log_level: LogLevel, cls_name, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.&f")[:-3]
        log = f"[{log_level.name}] [{cls_name}] [{now}] : {message}\n"
        print(log,end="")
        
        if self.file_path:
            with self.lock:
                with open(self.file_path, "a") as file:
                    file.write(log)

class Logger():
    def __init__(self, log_handler, cls_name):
        self.cls_name = cls_name
        self.log_handler = log_handler
    
    def log(self, log_level: LogLevel, message):
        if not isinstance(log_level, LogLevel):
            raise TypeError("Log level should be LogLevel type")
        if log_level >= self.log_handler.log_level:
            self.log_handler.log(log_level, self.cls_name, message)

class TestHanlder():
    def __init__(self, log_handler: LogHandler):
        self.logger = log_handler.get_logger(self)
    
    def start_process(self):
        self.logger.log(LogLevel.DEBUG, "Process 1 started..")
        self.logger.log(LogLevel.INFO, "Process 2 started..")
        self.logger.log(LogLevel.WARN, "Process 3 started..")
        self.logger.log(LogLevel.ALARM, "Process 4 started..")
        self.logger.log(LogLevel.ERROR, "Process 5 started..")
        
class TestAnalysis():
    def __init__(self, log_handler: LogHandler):
        self.logger = log_handler.get_logger(self)
        
    def start_analysys(self):
        self.logger.log(LogLevel.DEBUG, "Analysis 1 started")
        self.logger.log(LogLevel.INFO, "Analysis 2 started")
        self.logger.log(LogLevel.WARN, "Analysis 3 started")
        self.logger.log(LogLevel.ALARM, "Analysis 4 started")
        self.logger.log(LogLevel.ERROR, "Analysis 5 started")

if __name__ == "__main__":
    print("something")
    file_path = Path(f"Practices\\74_Log_Handler\\{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}-log.txt")
    handler = LogHandler(LogLevel.INFO, file_path=file_path)
    handler.log_level = LogLevel.WARN
    test_handler = TestHanlder(handler)
    test_analysis = TestAnalysis(handler)
    test_handler.start_process()
    test_analysis.start_analysys()
