# RasLeds
Control the built-in red and green LED's on Raspberry Pi Model 4 (Not sure if it works on Pi 3)
There is a blink.py for demo, either upload it directly to your pi and run or use start.sh for direct ssh

A good use for this is e.g:
- blink RED if audit trigger critical
- blink GREEN if priv-msg on IRC


To take control of your leds, ssh into your Pi and
```bash
echo none > /sys/class/leds/led0/trigger
echo none > /sys/class/leds/led1/trigger
```
Make /sys/class/leds/led*/* writable for user to skip using sudo

Permissions to the led* files are reverted after reboot. 
Use the ledpermission.service to fix at boot.
