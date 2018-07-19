from picamera import PiCamera
from time import sleep
from gpiozero import Button

camera = PiCamera()
camera.rotation = 180
button = Button(17)
camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/picamera/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        camera.close()
        break