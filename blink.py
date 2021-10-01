#!/bin/env python
"""
Make it blink
"""
import time

GREEN_FILE = "/sys/class/leds/led0/brightness"
RED_FILE = "/sys/class/leds/led1/brightness"

def write_leds(file, what):
    """ Write to files """
    what = 1 # always be red if not green
    if (what == "green"):
        what = 0
    with open(file, 'w') as run:
        run.write(what)

def blink(times, wait):
    """ blink """
    write_leds(GREEN_FILE, "green")
    write_leds(RED_FILE, "red")
    time.sleep(wait)
