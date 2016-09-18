import smbus
import time
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

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

while True:
	#Receive input from arduino
	number = readNumber()
	print number
	time.sleep(1)
