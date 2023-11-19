# Importing Libraries
import serial
import time

from time import sleep
import psutil

arduino = serial.Serial(port='/dev/pts/4', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    return

while True:
    ram=int(psutil.virtual_memory().percent * 2.55)
    cpu=int(psutil.cpu_percent() * 2.55)
    write_read(f"{ram},{cpu}\r")


    sleep(0.5)
    # break
