#!/usr/bin/python

print "I am python"
import RPi.GPIO as GPIO  
import time  
# blinking function  
def blink(pin):  
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(1)  
    return

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.OUT)
for i in range(0,5000):
    blink(11) 
GPIO.cleanup()
