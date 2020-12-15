import random
import sys
import time
from Adafruit_IO import MQTTClient
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)

ADAFRUIT_IO_KEY      = 'secretkey'       # Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'username'  # See https://accounts.adafruit.com

def connected(client):
    print('Connected...Listening...')
    client.subscribe('light')
    client.subscribe('TV')
    client.subscribe('Refrigerator')
    client.subscribe('Radiator')
def disconnected(client):
    print('Disconnected')
    sys.exit(1)

def message(client, feed_id, status):
    if feed_id == 'light':
        ##print(type(status),status)
        if status=='1':
            GPIO.output(7, GPIO.HIGH)
            print("Light is ON")
        elif status=='0':
            GPIO.output(7, GPIO.LOW)
            print("Light is OFF")
    elif feed_id == 'TV':
        if status=='1':
            GPIO.output(13,GPIO.HIGH)
            print("TV is ON")
        elif status=='0':
            GPIO.output(13, GPIO.LOW)
            print("TV is OFF")
    elif feed_id == 'Refrigerator':
        if status=='1':
            GPIO.output(16,GPIO.HIGH)
            print("Refrigerator is ON")
        elif status=='0':
            GPIO.output(16, GPIO.LOW)
            print("Refrigerator is OFF")
    elif feed_id == 'Radiator':
        if status=='1':
            GPIO.output(29,GPIO.HIGH)
            print("Radiator is ON")
        elif status=='0':
            GPIO.output(29, GPIO.LOW)
            print("Radiator is OFF")
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()
client.loop_blocking()