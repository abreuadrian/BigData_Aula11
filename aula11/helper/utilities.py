import time 
import os 

def time_clear (delay):
    time.sleep(delay)
    os.system('cls')

def error_msg(delay, txt=''):
    time_clear(delay)
    print(txt)

def clean():
    os.system('cls')