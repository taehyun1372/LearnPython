import time
import threading
class Process:
    def __init__(self):
        pass
    
    def process1(self, stop_event):
        for i in range(10):
            if stop_event.is_set():
                break
            else:
                time.sleep(1)
                print(f"must finish task {i}")
            
    def process2(self, stop_event):
        for i in range(10):
            if stop_event.is_set():
                break
            else:
                time.sleep(1)
            print(f"not important task {i}")
            
    
if __name__ == "__main__":
    process = Process()
        
    # print("main start")
    # thread1 = threading.Thread(target=process.process2, daemon=True) # finish when main thread finishes
    # thread1 = threading.Thread(target=process.process1, daemon=False) # last even after main thread finishes
    # thread1.start()
    # time.sleep(5)
    # print("main finish")
    
    # print("main start")
    # thread1 = threading.Thread(target=process.process2, daemon=True)
    # thread1.start()
    # thread1.join(timeout=5) # main task will process after 5 sec. Thread is still alive
    # print("this is main task")
    # print("main finish")
    
    print("main start")
    stop_event = threading.Event()
    thread1 = threading.Thread(target=process.process2, args=(stop_event,) ,daemon=True)
    thread1.start()
    thread1.join(timeout=5)
    if thread1.is_alive():
        print("Timeout occurred")
        stop_event.set() # send signal to thread to stop task
        thread1.join() # wait until thread finishes task
    print("this is main task")
    time.sleep(5)
    print("main task finish")