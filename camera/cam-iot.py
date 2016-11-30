#!/usr/bin/python

import picamera
import sys
import os
import time
import datetime
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIR_PIN = 12
GPIO.setup(PIR_PIN, GPIO.IN)

blob_service = BlockBlobService(account_name='myiothubiv', account_key='o8IeKnrSSbbyTWBnCJfkRiYMy1x2MICwRB00a6nXZ/YczkTCBFiMnAsxaEPljH8raOBuPj70H3Bv0O07GtAN6Q==')


while 1:

    if GPIO.input(PIR_PIN):

        print 'Motion detected!'
    
        time.sleep(2)
        camera = picamera.PiCamera()
        camera.resolution = (1024, 768)
    
        now = datetime.datetime.now()
        file_img = str(now) + ".jpg"
        camera.capture(file_img)

        print 'Uploading photo ' + file_img 
        try:
            blob_service.create_blob_from_path('img', file_img, file_img, content_settings=ContentSettings(content_type='image/jpeg'))
            print 'Done'
            os.remove(file_img)
        except:
            print 'Copy ' + file_img + ' to Azure BLOB failed'
            print(sys.exc_info()[1])

        camera.close()
        print 'Waiting for the motion...' 
        time.sleep(10)

