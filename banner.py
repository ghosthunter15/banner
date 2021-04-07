# #!/usr/bin/env/python3.9.1

import sys
import os
import subprocess
from time import sleep
from random import random
import psutil as ps
from termcolor import colored

# clear screen
subprocess.run(['clear'])

# freek me out
subprocess.run(['espeak', 'You have been hacked.'])

GREEN, RED, END = '\033[32;2m', '\033[31;1m',  '\033[0m'
sys.stdout.write(GREEN + """
         ____ _               _   _   _             _
        / ___| |__   ___  ___| |_| | | |_   _ _ __ | |_ ___ _ __
       | |  _| '_ \ / _ \/ __| __| |_| | | | | '_ \| __/ _ \ '__|
       | |_| | | | | (_) \__ \ |_|  _  | |_| | | | | ||  __/ |
        \____|_| |_|\___/|___/\__|_| |_|\__,_|_| |_|\__\___|_|
        \n\n"""
            + END)

# system info
p = ps.Process()

print('STATUS:\t\t', p.status(), '\n')
sleep(2)
print('Username:\t', os.getlogin())
print('Encoding:\t', sys.getfilesystemencoding())
print('User id:\t', p.uids())
print('Groupe:\t\t', p.gids())
print('Cpu times:\t', p.cpu_times())
print('Mem info:\t', p.memory_full_info())
print('CPU count:\t', ps.cpu_count())
print('\t\tBattery status.')
subprocess.run(['termux-battery-status'])
print('\t\t Printing working dir.\n', '\t', p.cwd(), '\n')
print('\t\t Date:')  
subprocess.run(['date'])

# not in use
"""
print(os.uname())
print('virtual_memory\t', ps.virtual_memory()) # need to split
print('swap_memory\t', ps.swap_memory()) # not working, needs to split
print('DISK_USAGE\t', ps.disk_usage('/')) # works fine, may need split
"""

__msg = '\n\tWe do not forget, We do not forgive, We are Anonymous.\n\n'
__speed = 50  # wpm

for i in __msg:
    sys.stdout.write(colored(str(i), "green", attrs = ['bold']))
    sys.stdout.flush()
    # sleep(0.03)
    sleep(random()*10.0/__speed)  # sim'ed human typing.
