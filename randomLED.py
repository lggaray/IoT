import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

while True:
    LED = random.randint(20,21)
    print(LED)
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED, True)
    time.sleep(0.5)
    GPIO.output(LED, False)

