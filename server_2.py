#!/usr/bin/env python
import serial
from time import sleep
import psutil

TTY_PORT = "/dev/ttyACM0"
BAUDRATE=115200

# Open a serial connection (adjust the port and baudrate accordingly)
ser = serial.Serial(TTY_PORT, BAUDRATE)

# Function to send values to Arduino
def send_values(value1, value2):
    data = f"{value1},{value2}\n"
    print(data.strip())
    ser.write(data.encode())
    sleep(0.1)  # Allow time for Arduino to process

# Example: Send values 42 and 78
while True:
    ram=float(psutil.virtual_memory().percent)
    cpu=float(psutil.cpu_percent())
    send_values(ram, cpu)

    sleep(1)

# Close the serial connection
ser.close()


"""
arduino = serial.Serial(port=TTY_PORT, baudrate=BAUDRATE, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.1)
    resp = arduino.readline()
    return resp

for n in range(1,255,10):
    print(n)
    print(write_read(f"{n},{n}\r"))
    time.sleep(1)
# 255 and 2.55 are veruy uncertain
while True:
    break
    ram=int(psutil.virtual_memory().percent)
    cpu=int(psutil.cpu_percent())
    response = write_read(f"{ram},{cpu}\r")
    print(ram, cpu, response)

    sleep(0.5)
    # break
"""
