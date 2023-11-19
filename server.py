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
    time.sleep(0.05)
    resp = arduino.readline()
    return resp

while True:
    ram=int(psutil.virtual_memory().percent * 2.55)
    cpu=int(psutil.cpu_percent() * 2.55)
    response = write_read(f"{ram},{cpu}\r")
    print(response)

    sleep(0.5)
    # break
