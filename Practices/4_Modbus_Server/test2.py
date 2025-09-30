import subprocess
import time

while True:

    # run main.py
    print("Starting main.py...")
    proc = subprocess.Popen(["python", "main.py"])

    # wait 60 seconds
    time.sleep(10)

    # kill main.py if still running
    if proc.poll() is None:  # still running
        print("Stopping main.py...")
        proc.terminate()
        proc.wait()
        # wait 10 seconds
        time.sleep(30)