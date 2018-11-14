import RPi.GPIO as gpio


#Pins - Motor's controller
motorA_pin_forward = 10
motorB_pin_forward = 11
motorA_pin_backward = 12
motorB_pin_backward = 13


#Setting up pins
def init()
	gpio.setmode(gpio.BOARD)
	

	gpio.setup(7, gpio.OUT)
	gpio.setup(11, gpio.OUT)
	gpio.setup(13, gpio.OUT)
	gpio.setup(15, gpio.OUT)