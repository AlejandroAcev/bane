import RPi.GPIO as gpio
import time

#Pins - Motor's controller
#Marron
motorA_pin_forward = 4
#Rojo
motorB_pin_forward = 17
#Naranja
motorA_pin_backward = 27
#verde
motorB_pin_backward = 22


#Setting up pins
def init():
	gpio.setmode(gpio.BOARD)
	
	gpio.setup(motorA_pin_forward, gpio.OUT)
	gpio.setup(motorB_pin_forward, gpio.OUT)
	gpio.setup(motorA_pin_backward, gpio.OUT)
	gpio.setup(motorB_pin_backward, gpio.OUT)


def forward():
	init()
	gpio.output(motorA_pin_forward, True)
	gpio.output(motorB_pin_forward, True)
	gpio.output(motorA_pin_backward, False)
	gpio.output(motorB_pin_backward, False)
	time.sleep(3)
	

def reverse():
	init()
	gpio.output(motorA_pin_forward, False)
	gpio.output(motorB_pin_forward, False)
	gpio.output(motorA_pin_backward, True)
	gpio.output(motorB_pin_backward, True)
	time.sleep(3)

print("Hacia adelante")
forward()
time.sleep(2)
print("Hacia atras")
reverse()