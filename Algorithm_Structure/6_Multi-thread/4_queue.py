import queue
import threading
import time

def work(message, sleep_time):
    print(f"{message} started")
    for i in range(sleep_time):
        print(f"{i}s elapsed..")
        time.sleep(1)
    print(f"{message} ended")

def process_work(q:queue.Queue):
    while True:
        item = q.get()
        if item is None:
            return
        item[0](*item[1])
        q.task_done()
        

if __name__ == "__main__":
    q = queue.Queue()
    for i in range(5):
        q.put([work, (f"work {i}", 5)])

    threads = []
    th1 = threading.Thread(target=process_work, args=(q, ))
    th1.start()
    threads.append(th1)

    th2 = threading.Thread(target=process_work, args=(q, ))
    th2.start()
    threads.append(th2)

    q.join()
    for i in range(2):
        q.put(None)

    for t in threads:
        t.join()