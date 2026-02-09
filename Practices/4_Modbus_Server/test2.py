import subprocess
import time

while True:

    # run TLSVersion.py
    print("Starting TLSVersion.py...")
    proc = subprocess.Popen(["python", "TLSVersion.py"])

    # wait 60 seconds
    time.sleep(10)

    # kill TLSVersion.py if still running
    if proc.poll() is None:  # still running
        print("Stopping TLSVersion.py...")
        proc.terminate()
        proc.wait()
        # wait 10 seconds
        time.sleep(30)