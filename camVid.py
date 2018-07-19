import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
#camera.capture('example.jpg')
camera.start_recording('example.h264')
time.sleep(5)
camera.stop_recording
camera.close()
