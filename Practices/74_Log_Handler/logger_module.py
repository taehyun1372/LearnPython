import logging
from datetime import datetime

# logging.basicConfig(
#     level=logging.INFO,
#     filename=f"Practices\\74_Log_Handler\\{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log",
#     filemode="a",
#     encoding="utf-8"
# )

# logging.info("Process started")
# logging.warning("Temperature is high")
# logging.info("Communication failed")

# logger = logging.getLogger("Process 1")

# logger.debug("Process started")
# logger.info("Process started")

class TestHandler():
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.INFO)
        
    def start_test(self):
        self.logger.debug("process 1 started")
        self.logger.info("process 2 started")
        self.logger.warning("process 3 started")
        self.logger.critical("process 4 started")
        self.logger.error("process 5 started")
        
class TestAnalysis():
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.WARN)
        
    def start_anlaysis(self):
        self.logger.debug("analysis 1 started")
        self.logger.info("analysis 2 started")
        self.logger.warning("analysis 3 started")
        self.logger.critical("analysis 4 started")
        self.logger.error("analysis 5 started")
        
if __name__ == "__main__":
    print("started")
    
    logging.basicConfig(
        level=logging.INFO,
        filename=f"Practices\\74_Log_Handler\\{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log",
        filemode="a",
        format= "[%(levelname)s] [%(name)s] [%(asctime)s] : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8"
    )
    
    test_handler = TestHandler()
    test_analysis = TestAnalysis()
    
    test_handler.start_test()
    test_analysis.start_anlaysis()