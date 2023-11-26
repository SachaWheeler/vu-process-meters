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
    # print(data.strip())
    ser.write(data.encode())
    sleep(0.1)  # Allow time for Arduino to process

print("Server running...")
while True:
    ram=float(psutil.virtual_memory().percent)
    cpu=float(psutil.cpu_percent())
    send_values(ram, cpu)

    sleep(1)

# Close the serial connection
ser.close()

