import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
'''
camera.start_preview()
time.sleep(5)
camera.capture('example.jpg')
camera.stop_preview()
camera.close()
'''

camera.start_preview()
camera.annotate_text = 'Hello world'
time.sleep(5)
camera.caputure('/home/pi/Desktop/text.jpg')
camera.stop_preview()
