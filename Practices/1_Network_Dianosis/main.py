import subprocess
import platform
import time

def ping_device(ip_address, count=4):
    param = '-t' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, ip_address]

    try :
        process = subprocess.Popen(command)
        print("Pining...Press Ctrl+C to stop")

        while True:
            time.sleep(1)
            if process.poll() is not None:
                break


        # if result.returncode == 0:
        #     print(f"Ping to {ip_address} succeeded:\n")
        #     print(result.stdout)
        # else:
        #     print(f"Ping to {ip_address} failed:\n")
        #     print(result.stdout)
        #     print(result.stderr)
    except KeyboardInterrupt:
        print("Stopping ping...")
        process.terminate()
        process.wait()
        print("Ping stopped")

if __name__ =="__main__":
    ip = input("Enter IP address to ping: ")
    ping_device(ip)





