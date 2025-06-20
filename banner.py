#!/usr/bin/env python3

# stdlib
import sys
import os
import subprocess
import json
from random import random
from time import sleep

# 3rd party lib
import psutil as ps

# clear screen
subprocess.run(["clear"])

# freek me out
# subprocess.run(["espeak", "You have been hacked."])

# Color codes
GREEN, RED, END = "\033[32;2m", "\033[31;1m", "\033[0m"

# Banner
sys.stdout.write(
    GREEN
    + """
         ____ _               _   _   _             _
        / ___| |__   ___  ___| |_| | | |_   _ _ __ | |_ ___ _ __
       | |  _| '_ \\ / _ \\/ __| __| |_| | | | | '_ \\| __/ _ \\ '__|
       | |_| | | | | (_) \\__ \\ |_|  _  | |_| | | | | ||  __/ |
        \\____|_| |_|\\___/|___/\\__|_| |_|\\__,_|_| |_|\\__\\___|_|
        \n\n"""
    + END
)

# System info
p = ps.Process()

# print("STATUS:\t\t", p.status(), "\n")
# sleep(2)


# Visual separator
def section_title(title):
    print(f"\n{GREEN}{'='*10} {title} {'='*10}{END}")


section_title("🖥 SYSTEM STATUS")

p = ps.Process()

# Process status
print(f"{GREEN}⚙️ Status:     {END}{p.status()}")

# User info
try:
    print(f"{GREEN}👤 Username:   {END}{os.getlogin()}")
except OSError:
    print(f"{RED}👤 Username:   Not available (possibly because kali){END}")

print(f"{GREEN}⌨️ Encoding:   {END}{sys.getfilesystemencoding()}")

# User/group info
uids = ", ".join([f"{k}={v}" for k, v in p.uids()._asdict().items()])
gids = ", ".join([f"{k}={v}" for k, v in p.gids()._asdict().items()])
print(f"{GREEN}🔐 User IDs:   {END}{uids}")
print(f"{GREEN}🔐 Group IDs:  {END}{gids}")

# CPU and memory info
cpu_times = p.cpu_times()
mem_info = p.memory_full_info()

print(
    f"{GREEN}🧮 CPU Times:  {END}user={cpu_times.user},\
        system={cpu_times.system}"
)
print(
    f"{GREEN}🧠 Memory:     {END}rss={mem_info.rss:,}\
        bytes, vms={mem_info.vms:,} bytes"
)

# Battery status
print("\n🔋 Battery status:")
try:
    output = subprocess.check_output(["termux-battery-status"], text=True)
    battery_data = json.loads(output)

    percentage = battery_data.get("percentage")
    status = battery_data.get("status")

    percent_color = GREEN if percentage > 20 else RED
    status_color = GREEN if status in ("CHARGING", "FULL") else RED

    print(f"   Battery: {percent_color}{percentage}%{END}")
    print(f"   Status : {status_color}{status}{END}")

except FileNotFoundError:
    print(f"{RED}termux-battery-status not found. Install Termux:API.{END}")
except json.JSONDecodeError as e:
    print(f"{RED}JSON error: {e}{END}")
except Exception as e:
    print(f"{RED}Unexpected error: {e}{END}")

# Working directory and date
print("\n📂 Printing working dir:\t", p.cwd(), "\n")
print("📅 Date:")
subprocess.run(["date"])

# from termcolor import colored

# bat = subprocess.run(['termux-battery-status'])

"""
In testing...
Does not work on android

battery = p.sensors_battery()

if battery is None:
    print("Battery information unavailable.")
else:
    print("Battery percentage:", battery.percent)
    print("Power plugged in:", battery.power_plugged)
    print("Seconds left:", battery.secsleft)
"""

"""
print(os.uname())
print('virtual_memory\t', ps.virtual_memory()) # need to split
print('swap_memory\t', ps.swap_memory()) # not working, needs to split
print('DISK_USAGE\t', ps.disk_usage('/')) # works fine, may need split
"""

__wpm__ = 45  # typing speed.
__msg__ = "\n\tWe do not forget, We do not forgive, We are Anonymous.\n\n"

for i in __msg__:
    # sys.stdout.write(colored(str(i), "green", attrs = ['bold']))
    sys.stdout.write(GREEN + str(i) + END)
    sys.stdout.flush()
    sleep(random() * 10.0 / __wpm__)

"""
import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ''
"""
