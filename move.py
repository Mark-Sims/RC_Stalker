import RPi.GPIO as GPIO
import time
import random

def move_bootstrap():
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(8, GPIO.OUT)
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)

def turn_left():
	GPIO.output(12, True)
	GPIO.output(15, True)
	time.sleep(0.3)
	GPIO.output(12, False)
	GPIO.output(15, False)

def turn_right():
	GPIO.output(8, True)
	GPIO.output(10, True)
	time.sleep(0.3)
	GPIO.output(8, False)
	GPIO.output(10, False)
	
def forward():
	GPIO.output(7, True)

def stop():
	GPIO.output(7, False)
move_bootstrap()
forward()
time.sleep(5)
turn_right()
time.sleep(2)
turn_left()
time.sleep(2)
stop()

		
