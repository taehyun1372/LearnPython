import queue
import threading
import time

def work(message, sleep_time):
    print(f"{message} started")
    for i in range(sleep_time):
        print(f"{i}s elapsed..")
        time.sleep(1)
    print(f"{message} ended")

if __name__ == "__main__":
    th1 = threading.Thread(target=work, args=("work1", 5))
    th1.daemon = False
    th1.start()

    th2 = threading.Thread(target=work, args=("work2", 7))
    th2.daemon = False
    th2.start()

    th1.join()
    th2.join()
    print("Main thread finishes here")