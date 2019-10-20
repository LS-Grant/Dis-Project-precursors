#program is used to turn on the LEDs to test
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17,True)
GPIO.output(18,True)
GPIO.output(22,True)