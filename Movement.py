import RPi.GPIO as gpio
import time as Time

#Pins - Motor's controller
MOTOR_1_PIN_FORWARD = 12
MOTOR_1_PIN_BACKWARD = 11
MOTOR_2_PIN_FORWARD = 13
MOTOR_2_PIN_BACKWARD = 15

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n") 

class Motor:
	"""
	Motor
	"""
	def __init__(self, pin1, pin2):
		self.pin1 = pin1
		self.pin2 = pin2

def move_forward(motor1, motor2, time):
	gpio.output(motor1.pin1, gpio.HIGH)
	gpio.output(motor1.pin2, gpio.LOW)
	gpio.output(motor2.pin1, gpio.HIGH)
	gpio.output(motor2.pin2, gpio.LOW)
	Time.sleep(time)

def move_backward(motor1, motor2, time):
	gpio.output(motor1.pin1, gpio.LOW)
	gpio.output(motor1.pin2, gpio.HIGH)
	gpio.output(motor2.pin1, gpio.LOW)
	gpio.output(motor2.pin2, gpio.HIGH)
	Time.sleep(time)

def stop(motor1, motor2):
	gpio.output(motor1.pin1, gpio.LOW)
	gpio.output(motor1.pin2, gpio.LOW)
	gpio.output(motor2.pin1, gpio.LOW)
	gpio.output(motor2.pin2, gpio.LOW)


if __name__ == '__main__':
	gpio.setmode(gpio.BOARD)

	# Setting up motor 1 pins
	gpio.setup(MOTOR_1_PIN_FORWARD, gpio.OUT)
	gpio.setup(MOTOR_1_PIN_BACKWARD, gpio.OUT)
	gpio.output(MOTOR_1_PIN_FORWARD, gpio.LOW)
	gpio.output(MOTOR_1_PIN_BACKWARD, gpio.LOW)

	# Setting up motor 2 pins
	gpio.setup(MOTOR_2_PIN_FORWARD, gpio.OUT)
	gpio.setup(MOTOR_2_PIN_BACKWARD, gpio.OUT)
	gpio.output(MOTOR_2_PIN_FORWARD, gpio.LOW)
	gpio.output(MOTOR_2_PIN_BACKWARD, gpio.LOW)
	motor1 = Motor(MOTOR_1_PIN_FORWARD, MOTOR_1_PIN_BACKWARD)
	motor2 = Motor(MOTOR_2_PIN_FORWARD, MOTOR_2_PIN_BACKWARD)
	print("Starting")
	move_forward(motor1, motor2, 3)
	print("Stopping")
	stop(motor1, motor2)
	print("Starting")
	move_backward(motor1, motor2, 3)
	print("Stopping")
	stop(motor1, motor2)
	gpio.cleanup()