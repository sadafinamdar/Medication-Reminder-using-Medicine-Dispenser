import RPi.GPIO as GPIO
import time ,os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1_1 = 15    # Input Pin
Motor1_2 = 18    # Input Pin

Motor2_1 =25    # Input Pin
Motor2_2 =8    # Input Pin

Motor3_1 = 23    # Input Pin
Motor3_2 = 24    # Input Pin

GPIO.setup(Motor1_1,GPIO.OUT)
GPIO.setup(Motor1_2,GPIO.OUT)
GPIO.setup(Motor2_1,GPIO.OUT)
GPIO.setup(Motor2_2,GPIO.OUT)
GPIO.setup(Motor3_1,GPIO.OUT)
GPIO.setup(Motor3_2,GPIO.OUT)

GPIO.output(Motor1_1,GPIO.LOW)
GPIO.output(Motor1_2,GPIO.LOW)
GPIO.output(Motor2_1,GPIO.LOW)
GPIO.output(Motor2_2,GPIO.LOW)
GPIO.output(Motor3_1,GPIO.LOW)
GPIO.output(Motor3_2,GPIO.LOW)


try:
	while 1:
		GPIO.output(Motor1_1,GPIO.LOW)
		GPIO.output(Motor1_2,GPIO.LOW)
		GPIO.output(Motor2_1,GPIO.LOW)
		GPIO.output(Motor2_2,GPIO.LOW)
		GPIO.output(Motor3_1,GPIO.HIGH)
		GPIO.output(Motor3_2,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.cleanup()


