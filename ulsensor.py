import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 13
echo = 26

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

'''
servo
'''

pin_pwm = 18
frequency = 50
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin_pwm, GPIO.OUT)
p = GPIO.PWM(pin_pwm, frequency)
p.start(0)

#ultra-sonic
try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.05)
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            start = time.time()
        while GPIO.input(echo) == 1:
            end = time.time()

        duration = end-start
        distance = round((duration*340*100)/2, 2)

        print("Distance: ", distance,"cm")

        if distance <= 5:
            try:
                dc = 0
                min_dc = 2.2
                max_dc = 11.5
                change_step = 10
                change = float((max_dc-min_dc)/change_step)
                toggle = 1
                delay = 0.4
                dc = min_dc

                while True:
                    p.ChangeDutyCycle(dc)

                    #show curent angle
                    print('angle: %d '%((dc-min_dc)*180/(max_dc-min_dc)-90))#,end='\r')
                    time.sleep(delay)

                    #to make servo moves like windscreen wipe
                    if dc + change <= max_dc and toggle:
                        dc += change
                    
                    elif dc-change >= min_dc:
                        dc -= change
                        toggle = 0
                    else:
                        dc += change
                        toggle = 1
            except:
                GPIO.cleanup()

except:
    GPIO.cleanup()

