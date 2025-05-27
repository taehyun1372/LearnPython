import subprocess
import platform
import time
import signal
import threading

def stream_output(process, command, display_live):
    last_lines = []
    for line in process.stdout:
        if (display_live):
            print(line)

        if len(last_lines) < 15:
            last_lines.append((line))
        else:
            last_lines.pop(0)
            last_lines.append(line)

    find_statistics(last_lines, command)

    process.stdout.close()

def ping_device(ip_addresses, display_live):
    commands = []
    for ip_address in ip_addresses:
        commands.append(['ping', '-t', ip_address])

    try :
        output_lines = []
        processes = []
        threads = []
        for command in commands:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            processes.append(process)
            thread = threading.Thread(target=stream_output, args=(process, command, display_live))
            thread.start()
            threads.append(thread)

        print("Pining...Press Ctrl+C to stop")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nCtrl+C pressed, sending interrupt to ping subprocess...")

        # try:
        #     process.send_signal(signal.SIGINT)
        # except Exception as e:
        #     print("Failed to send SIGINT to subprocess:", e)

        print("Waiting for the result")
        # for thread in threads:
        #     thread.join()

        print("The programme ended")

def find_statistics(last_lines, command):
    lines = ""

    for line in last_lines:
        lines += line

    statisticsIndex = lines.index("statistics")
    packetIndex = lines.index("Packets:", statisticsIndex)

    sentIndex = lines.index("Sent", packetIndex)
    sentText = "Sent = "
    sentPacketIndex = sentIndex + len(sentText)
    sentPacketLength = lines.index(",", sentPacketIndex) - sentPacketIndex
    sentPacket = lines[sentPacketIndex]

    receiveIndex = lines.index("Received", sentIndex)
    receiveText = "Received = "
    receivePacketIndex = receiveIndex + len(receiveText)
    receivePacketLength = lines.index(",", receivePacketIndex) - receivePacketIndex
    receivePacket = lines[receivePacketIndex]

    print(f"## Statistics : {command} sent : {sentPacket} and Received {receivePacket} ##")

if __name__ =="__main__":
    # ip = input("Enter IP address to ping: ")
    IPs = []
    IPs.append("192.168.1.101")
    ping_device(IPs, False)





