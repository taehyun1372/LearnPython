from multiprocessing import Process
import time

def worker(name, elapse):
    print(f"{name} started")
    for i in range(elapse):
        print(f"{name}: {i}")
        time.sleep(1)
    print(f"{name} finished")

if __name__ == "__main__":
    p1 = Process(target=worker, args=("Process-1", 5))
    p2 = Process(target=worker, args=("Process-2", 10))
    processes = []
    processes.append(p1)
    processes.append(p2)
    p1.start()
    p2.start()
    time_limit = 7
    count = 0
    start = time.monotonic()
    while True:
        elapsed = time.monotonic() - start
        if elapsed > time_limit:
            for p in processes:
                if p.is_alive():
                    (print(f"Time limit occurred. Terminating process..{p}"))
                    p.terminate()
            for p in processes:
                p.join()
            break
        time.sleep(1)
                
    print("main finished")