#!/bin/env python3

import sys
import time

led_red_file = "/sys/class/leds/led1/brightness"
led_green_file = "/sys/class/leds/led0/brightness"
times = 0

def led_status(stat, led):
	if (stat == 1):
		if (led == "red"):
			f = open(led_red_file, 'w')
			f.write('1')
			f.close()
		elif (led == "green"):
			f = open(led_green_file, 'w')
			f.write('1')
			f.close()
		else:
			exit()
	if (stat == 0):
		if (led == "red"):
			f = open(led_red_file, 'w')
			f.write('0')
			f.close()
		elif (led == "green"):
			f = open(led_green_file, 'w')
			f.write('0')
			f.close()
		else:
			exit()

def led_on(led):
	if (led == "red"):
		f = open(led_red_file, 'w')
		f.write('1')
		f.close()
	elif (led == "green"):
		f = open(led_green_file, 'w')
		f.write('1')
		f.close()
	else:
		print("Wrong led")
		exit()

def led_off(led):
	if (led == "red"):
		f = open(led_red_file, 'w')
		f.write('0')
		f.close()
	elif (led == "green"):
		f = open(led_green_file, 'w')
		f.write('0')
		f.close()
	else:
		print("Wrong led")
		exit()


def led_blink(times, long):
	for i in range(times):
		# Green On, Red Off
		time.sleep(long)
		led_on('green')
		led_off('red')
		# Red On, Green Off
		time.sleep(long)
		led_off('green')
		led_on('red')


led_blink(5, 0.4)

# Reset to zero
led_off('green')
led_off('red')
