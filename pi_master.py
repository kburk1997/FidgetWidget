import subprocess
import smbus
import time
import RPi.GPIO as GPIO
from Tkinter import *

WINDOW_W=700
WINDOW_H=500

BLUE='#a6def2'

def createDisplay():
	global tk
	tk=Tk()
	canvas=Canvas(tk, width=WINDOW_W, height=WINDOW_H, background=BLUE)
	canvas.pack()
	tk.mainloop()

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
	return	
def button():
	return

createDisplay()

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
	if(GPIO.input(4)):
		#change color
		print "LDR Procedure"
		LDR()
	#otherwise, check buttons
	if(!GPIO.input(18) || !GPIO.input(23) || !GPIO.input(24)):
		#go to button procedure
		print "Button procedure"
		button()
	time.sleep(0.5)
	
def terminate():
	global tk
	tk.destroy()
