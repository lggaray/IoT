import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
'''
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,5000)
pwm.start(0)

a=0
while a<100:
    pwm.ChangeDutyCycle(a)
    print(a)
    a+=1
    time.sleep(0.05)
GPIO.cleanup()
pwm.stop()
'''

LED = 18
GPIO.setup(LED,GPIO.OUT)
p = GPIO.PWM(LED,100)
p.start(0)

try:
    while True:
        for val in range(0,101,5):
            p.ChangeDutyCycle(val)
            print(val)
            time.sleep(0.2)
except:
    print('Error')

finally:
    p.stop()
    GPIO.cleanup()
