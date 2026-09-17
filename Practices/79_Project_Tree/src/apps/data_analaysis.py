# from common.tcp import TCP
# from libraries.nfc import NFC
import sys
import os

class DataAnalysis:
    def __init__(self):
        pass
    
    def run(self):
        print("Data analysis")
    
if __name__ == "__main__":   
    print("----System paths----")
    for path in sys.path:
        print(path)
        
    from manufacturing import Manufacturing
    manu = Manufacturing()
        
    # with open("config.txt") as f:
    #     for line in f:
    #         print(line)
    
    print(f"Current working directory is {os.getcwd()}")
    
    with open("ReadMe.txt") as f:
        for line in f:
            print(line)
    
    from monitor import Monitor
    mon = Monitor()