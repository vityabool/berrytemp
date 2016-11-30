#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 12

GPIO.setup(PIR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(PIR_PIN):
            print 'Motion Detected!'
            time.sleep(1)
except KeyboardInterrupt:
    print 'Quit'
    GPIO.cleanup()



