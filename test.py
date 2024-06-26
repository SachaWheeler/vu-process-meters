#!/usr/bin/env python
import serial
from time import sleep
import psutil
import os

os.popen('gnome-screensaver-command --lock')


ram=float(psutil.virtual_memory().percent)
cpu=float(psutil.cpu_percent())

print(f"""
{psutil.cpu_percent()=}
{psutil.virtual_memory()=}
{psutil.cpu_count()=}
{psutil.cpu_stats()=}
{psutil.cpu_freq()=}
{psutil.getloadavg()=}
{psutil.disk_usage('/')=}
{psutil.disk_usage('/').percent=}

        """)

