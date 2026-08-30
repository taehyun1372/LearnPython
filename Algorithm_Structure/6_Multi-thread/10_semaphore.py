import threading
import time

class ThreadPool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()
        self.count = 0

    def acquire(self, name):
        with self.lock:
            self.active.append(name)
            for i in range(10):
                temp = self.count
                time.sleep(0)
                self.count = temp + 1
            print("Acquired: {0} | thread pool: {1}".format(name, self.active))

    def release(self, name):
        with self.lock:
            self.active.remove(name)
            print("Released: {0} | thread pool: {1}".format(name, self.active))

def worker(semaphore, pool):
    with semaphore:
        name = threading.current_thread().name
        pool.acquire(name)
        pool.release(name)

if __name__ == "__main__":
    threads = []
    pool = ThreadPool()
    semaphore = threading.Semaphore(10)
    for i in range(100):
        t = threading.Thread(
            target = worker, name="Thread " + str(i), args=(semaphore, pool)
        )
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    print(pool.count)
    print(pool.count)
    print(pool.count)