#Program is used to turn of the LEDs
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17,False)
GPIO.output(18,False)
GPIO.output(22,False)