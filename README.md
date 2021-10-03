# RasLeds
Control the built-in red and green LED's on Raspberry Pi Model 4 (Not sure if it works on Pi 3)  
There is a blink.py for demo, either upload it directly to your pi and run or use start.sh for direct ssh

A good use for this is
- Turn RED ON if audit trigger critical event
- blink GREEN if priv-msg on IRC


To take control of your leds, ssh into your Pi and
```bash
sudo echo none > /sys/class/leds/led0/trigger
sudo echo none > /sys/class/leds/led1/trigger
```
Make /sys/class/leds/led*/brightness writable for user to skip using sudo
```bash
sudo chmod a+w /sys/class/leds/led*/brightness
```
Permissions to the led* files are reverted after reboot.  
Use the included ledpermission.service to set write permissions at userspace.
