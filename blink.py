#!/bin/env python3
"""
Blink blink ;) ;)
"""
from time import sleep

RED_FILE = "/sys/class/leds/led1/brightness"
GREEN_FILE = "/sys/class/leds/led0/brightness"
times = 0


def write(file, res):
    if file == "red":
        f = open(RED_FILE, 'w')
        f.write(res)
        f.close()
    if file == "green":
        f = open(GREEN_FILE, 'w')
        f.write(res)
        f.close


def led_on(led):
    # Turn on led
    if (led == "red"):
        write("red", "1")
    elif (led == "green"):
        write("green", "1")
    else:
        print("Wrong led")
        exit()


def led_off(led):
    # Turn off led
    if (led == "red"):
        write("red", "0")
    elif (led == "green"):
        write("green", "0")
    else:
        print("Wrong led")
        exit()


def led_blink(times, long):
    # Calls led_on/off for [times] every [long]
    for i in range(times):
        # Green On, Red Off
        sleep(long)
        led_on('green')
        led_off('red')
        # Red On, Green Off
        sleep(long)
        led_off('green')
        led_on('red')


led_blink(5, 0.4)

# Reset to zero
led_off('green')
led_off('red')