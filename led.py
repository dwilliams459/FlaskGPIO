# Python Script to enable/disable pins on Raspberry PI

import RPi.GPIO as GPIO  
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

time.sleep(1)

try:
  for x in range(0, 100):
    print(x)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(.05)
    GPIO.output(18,GPIO.LOW)
    time.sleep(.05)

finally:
  GPIO.cleanup()

