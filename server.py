#!/usr/bin/env python3
import serial
# pip install pySerial
import subprocess
from time import sleep
import psutil

TTY_PORT = "/dev/ttyACM0"
BAUDRATE = 115200
UPDATE_DELAY = 1
screensaver = 0
prev_screensaver = screensaver

ser = serial.Serial(TTY_PORT, BAUDRATE)

io = psutil.net_io_counters()
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

def send_values(ram, cpu, up, dn, screensaver):
    # \1 and \2 are up and down arrows defined in the arduino
    data = (f"{screensaver}"
            f"R {ram:>4}%  \1{get_size(up):>6},"
            f"C {cpu:>4}%  \2{get_size(dn):>6}\n")

    ser.write(data.encode())

def get_size(bytes):
    for unit in ['B', 'K', 'M', 'G']:
        if bytes < 1024:
            if bytes >= 1000:
                return f"{bytes/UPDATE_DELAY:.0f} {unit}"
            else:
                return f"{bytes/UPDATE_DELAY:.1f}{unit}"
        bytes /= 1024

print("Server running...")
while True:
    sleep(UPDATE_DELAY)
    locked = subprocess.Popen(['gnome-screensaver-command', '-q'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    # print(locked.communicate()[0])
    screensaver = 0 if 'inactive' in str(locked.communicate()[0]) else 1

    if screensaver == 0 or screensaver != prev_screensaver:
        ram = float(psutil.virtual_memory().percent)
        cpu = float(psutil.cpu_percent())

        io_2 = psutil.net_io_counters()
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

        # update values
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
        prev_screensaver = screensaver
        # print("updating")
    send_values(ram, cpu, us, ds, screensaver)

    if ser.in_waiting:
        command = ser.readline().decode().strip()
        print("Received command:", command)

ser.close()

