# Importing Libraries
import serial
import time

from time import sleep
import psutil

TTY_PORT = "/dev/ttyACM0"
BAUDRATE=115200

arduino = serial.Serial(port=TTY_PORT, baudrate=BAUDRATE, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.1)
    resp = arduino.readline()
    return resp

for n in range(1,255,10):
    print(n)
    print(write_read(f"{n},{n}\r"))
    time.sleep(2)
# 255 and 2.55 are veruy uncertain
while True:
    break
    ram=int(psutil.virtual_memory().percent)
    cpu=int(psutil.cpu_percent())
    response = write_read(f"{ram},{cpu}\r")
    print(ram, cpu, response)

    sleep(0.5)
    # break
