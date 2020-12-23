#!/usr/bin/env/python3.6

import sys
import subprocess
from time import sleep
from termcolor import colored

subprocess.run(['clear'])

GREEN, RED, END = '\033[32;2m', '\033[31;1m',  '\033[0m'
sys.stdout.write(GREEN + """
             ____ _               _   _   _             _
            / ___| |__   ___  ___| |_| | | |_   _ _ __ | |_ ___ _ __
           | |  _| '_ \ / _ \/ __| __| |_| | | | | '_ \| __/ _ \ '__|
           | |_| | | | | (_) \__ \ |_|  _  | |_| | | | | ||  __/ |
            \____|_| |_|\___/|___/\__|_| |_|\__,_|_| |_|\__\___|_|
            \n\n"""
            + END)

__msg__ = 'We do not forget, We do not forgive, We are Anonymous.\n\n'
for i in __msg__:
    sys.stdout.write(colored(str(i), "green", attrs = ['bold']))
    sys.stdout.flush()
    sleep(0.03)

