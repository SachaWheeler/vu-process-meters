#!/usr/bin/env python
import serial
from time import sleep
import psutil

TTY_PORT = "/dev/ttyACM0"
BAUDRATE = 115200
UPDATE_DELAY = 1

# Open a serial connection (adjust the port and baudrate accordingly)
ser = serial.Serial(TTY_PORT, BAUDRATE)

io = psutil.net_io_counters()
# extract the total bytes sent and received
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

# Function to send values to Arduino
def send_values(ram, cpu, up, down):
    # data = f"{ram},{cpu},{up},{down}\n"
    data = (f"R {ram:>4}%  {get_size(up):>7},"
            f"C {cpu:>4}%  {get_size(down):>7}\n")
    # print(data.strip())
    ser.write(data.encode())
    # 1sleep(0.1)  # Allow time for Arduino to process

# format bytes
def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes/UPDATE_DELAY:.1f}{unit}B"
        bytes /= 1024

print("Server running...")
while True:
    sleep(UPDATE_DELAY)

    ram = float(psutil.virtual_memory().percent)
    cpu = float(psutil.cpu_percent())

    io_2 = psutil.net_io_counters()
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

    send_values(ram, cpu, us, ds)
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

ser.close()

