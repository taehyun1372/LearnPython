from threading import Thread, Lock
import threading

count = 0

def worker(mutex, data, thread_safe):
    global count
    if thread_safe:
        mutex.acquire()
    try:
        count += 1
        print("thread {0}: {1}, {2}\n".format(threading.get_ident(), data, count))
    finally:
        if thread_safe:
            mutex.release()

if __name__ == "__main__":
    threads = []
    thread_safe = True
    mutex = Lock()
    for i in range(100):
        t = Thread(target=worker, args=(mutex, i, thread_safe))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()