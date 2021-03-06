import subprocess
import smbus
import time
import RPi.GPIO as GPIO
from Tkinter import *
import webbrowser

WINDOW_W=700
WINDOW_H=500

BLUE='#a6def2'

# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

#Setup GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	#'Hacky' fix for IOError
	try:
		bus.write_byte(address, value)
	except IOError:
		subprocess.call(['i2cdetect','-y','1'])
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number=0
	try:
		number = bus.read_byte(address)
	except IOError:
		subprocess.call(['i2cdetect','-y','1'])
	# number = bus.read_byte_data(address, 1)
	return number
	
def LDR():
	global tk, canvas
	print "LDR"
	createDisplay("wave.gif")
	check()
	return	
def button():
	createDisplay("spiral.gif")
	check()
	return

def check():
	if(GPIO.input(4)):
		#change color
		print "LDR Procedure"
		LDR()
	#otherwise, check buttons
	if(not GPIO.input(18) or not GPIO.input(23) or not GPIO.input(24)):
		#go to button procedure
		print "Button procedure"
		button()
def createDisplay(picture):
	webbrowser.open(picture)
	while(GPIO.input(4) or not GPIO.input(18) or not GPIO.input(23) or not GPIO.input(24)):
		pass

while True:
	#Receive input from arduino
	number = readNumber()
	print number
	print GPIO.input(18)
	print GPIO.input(23)
	print GPIO.input(24)
	
	#Read in the 4
	print GPIO.input(4)
	
	#if above threshold, start

	
	time.sleep(0.5)
	
def terminate():
	global tk
	tk.destroy()
