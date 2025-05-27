import subprocess
import sys
import time

p1 = subprocess.Popen(args=[sys.executable, "test_02.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(args=[sys.executable, "test_03.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
p3 = subprocess.Popen(args=[sys.executable, "test_04.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

input1 = input("Enter input 1>>")
output1, error1 = p1.communicate(input=input1)
print(output1)

input2 = input("Enter input 2>>")
output2, error2 = p2.communicate(input=input2)
print(output2)

input3 = input("Enter input 3>>")
p3.stdin.write(input3)
p3.stdin.close()
for line in p3.stdout:
    print("Live output:", line.strip())
