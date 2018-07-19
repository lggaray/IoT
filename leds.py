import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

try:
    a=1
    while a < 10:
        GPIO.output(26, True)
        time.sleep(1)
        GPIO.output(26, False)
        a+=1
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
