#!/usr/bin/env python
import serial
import subprocess
from time import sleep, process_time, time
import psutil

TTY_PORT = "/dev/ttyACM0"
BAUDRATE = 115200
UPDATE_DELAY = 1

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
start_time = time()
while True:
    sleep(0.05)
    if (time() - start_time) > UPDATE_DELAY:
        start_time = time()

        ram = float(psutil.virtual_memory().percent)
        cpu = float(psutil.cpu_percent())

        io_2 = psutil.net_io_counters()
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

        # update values
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
        locked = subprocess.Popen(['gnome-screensaver-command', '-q'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        # print(locked.communicate()[0])
        screensaver = 0 if 'inactive' in str(locked.communicate()[0]) else 1
        send_values(ram, cpu, us, ds, screensaver)

ser.close()

