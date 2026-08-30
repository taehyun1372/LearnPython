import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def work_1():
    print("[work 1] try to acquire lock a")
    with lock_a:
        print("[work 1] acquired lock a")

        time.sleep(1)

        print("[work 1] try to acquire lock b")
        with lock_b:
            print("[work 1] acquired lock b")

def work_2():
    print("[work 2] try to acquire lock b")
    with lock_b:
        print("[work 2] acquired lock b")

        time.sleep(1)

        print("[work 2] try to acquire lock a")
        with lock_a:
            print("[work 2] acquired lock a")

if __name__ == "__main__":
    print("started")
    th1 = threading.Thread(target=work_1)
    th1.start()
    th2 = threading.Thread(target=work_2)
    th2.start()
    th1.join()
    th2.join()
    print("finished")