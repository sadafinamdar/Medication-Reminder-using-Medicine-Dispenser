#!/usr/bin/python

def tablet1_dispenser():

					print("tablet 1")

					GPIO.output(LED,GPIO.HIGH)

					lcd.clear()

					lcd.write8(0x80)

					lcd.message('TABLET 1')

					os.system (' omxplayer Record-004.mp3')

					time.sleep(1) 

					GPIO.output(Motor1_1,GPIO.LOW)

					GPIO.output(Motor1_2,GPIO.HIGH)

					time.sleep(2) 

					GPIO.output(Motor1_1,GPIO.LOW)

					GPIO.output(Motor1_2,GPIO.LOW)

					time.sleep(0.5) 

					GPIO.output(Motor1_1,GPIO.HIGH)

					GPIO.output(Motor1_2,GPIO.LOW)

					time.sleep(2.2) 

					GPIO.output(Motor1_1,GPIO.LOW)

					GPIO.output(Motor1_2,GPIO.LOW)

					lcd.write8(0xC0)

					lcd.message('Sending mail..')

					os.system ("echo 'Time to Take Tablet 1' | mail -s 'MEDICINE DISPENSER' aagnihotri618@gmail.com")

					lcd.clear()

					return;

def tablet2_dispenser():

				print("tablet 2")

				GPIO.output(LED,GPIO.HIGH)

				lcd.clear()

				lcd.write8(0x80)

				lcd.message('TABLET 2')

				os.system (' omxplayer Record-002.mp3')

				time.sleep(1) 

				GPIO.output(Motor2_1,GPIO.LOW)

				GPIO.output(Motor2_2,GPIO.HIGH)

				time.sleep(2) 

				GPIO.output(Motor2_1,GPIO.LOW)

				GPIO.output(Motor2_2,GPIO.LOW)

				time.sleep(0.5) 

				GPIO.output(Motor2_1,GPIO.HIGH)

				GPIO.output(Motor2_2,GPIO.LOW)

				time.sleep(2.2) 

				GPIO.output(Motor2_1,GPIO.LOW)

				GPIO.output(Motor2_2,GPIO.LOW)

				lcd.write8(0xC0)

				lcd.message('Sending mail..')

				os.system ("echo 'Time to Take Tablet 2' | mail -s 'MEDICINE DISPENSER' aagnihotri618@gmail.com")

				lcd.clear()

				return;

def tablet3_dispenser():

				print("tablet 3")

				GPIO.output(LED,GPIO.HIGH)

				lcd.clear()

				lcd.write8(0x80)

				lcd.message('TABLET 3')

				os.system (' omxplayer Record-003.mp3')

				time.sleep(1) 

				GPIO.output(Motor3_1,GPIO.LOW)

				GPIO.output(Motor3_2,GPIO.HIGH)

				time.sleep(2) 

				GPIO.output(Motor3_1,GPIO.LOW)

				GPIO.output(Motor3_2,GPIO.LOW)

				time.sleep(0.5) 

				GPIO.output(Motor3_1,GPIO.HIGH)

				GPIO.output(Motor3_2,GPIO.LOW)

				time.sleep(2.2) 

				GPIO.output(Motor3_1,GPIO.LOW)

				GPIO.output(Motor3_2,GPIO.LOW)

				lcd.write8(0xC0)

				lcd.message('Sending mail..')

				os.system ("echo 'Time to Take Tablet 3' | mail -s 'MEDICINE DISPENSER' sadafinamdar98@gmail.com")

				lcd.clear()

				return;

	

import os 

from PIL import Image

import RPi.GPIO as GPIO

import time ,os

from picamera import PiCamera

import Adafruit_CharLCD as LCD

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)



############################

time1 = "13"

time2 = "13"

time3 = "13"

############################



Motor1_1 = 15    # Input Pin

Motor1_2 = 18    # Input Pin



Motor2_1 =25    # Input Pin

Motor2_2 =8    # Input Pin



Motor3_1 = 23    # Input Pin

Motor3_2 = 24    # Input Pin

LED 	=  14   # Input Pin

SWITCH 	= 21    # Input Pin



GPIO.setup(Motor1_1,GPIO.OUT)

GPIO.setup(Motor1_2,GPIO.OUT)

GPIO.setup(Motor2_1,GPIO.OUT)

GPIO.setup(Motor2_2,GPIO.OUT)

GPIO.setup(Motor3_1,GPIO.OUT)

GPIO.setup(Motor3_2,GPIO.OUT)

GPIO.setup(LED,GPIO.OUT)

GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)



GPIO.output(Motor1_1,GPIO.LOW)

GPIO.output(Motor1_2,GPIO.LOW)

GPIO.output(Motor2_1,GPIO.LOW)

GPIO.output(Motor2_2,GPIO.LOW)

GPIO.output(Motor3_1,GPIO.LOW)

GPIO.output(Motor3_2,GPIO.LOW)

GPIO.output(LED,GPIO.LOW)



lcd_rs = 12

lcd_en = 16

lcd_d4 = 6

lcd_d5 = 13

lcd_d6 = 19

lcd_d7 = 26

lcd_columns = 16

lcd_rows = 2





lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)



lcd.write8(0x80)

lcd.message('   MEDICINE   \n   DISPENSER')

time.sleep(2.0)

lcd.clear()

camera = PiCamera()

camera.resolution = (800, 600)



try:

	while 1:

		switch_val = GPIO.input(SWITCH)

		if os.path.exists("date.txt"):

			os.remove("date.txt")

		else:

			print("File doesnt exist")

		os.system("date >> date.txt")

		fo = open("date.txt", "r+")

		data  = fo.read(18);

		hr = data[11] + data[12]

		col = ':'

		m  = data[14] + data[15]

		timee =  hr+col+m

		print timee

		fo.close()

		lcd.write8(0x80)

		lcd.message('T:')

		lcd.message(timee)

		lcd.message('')





		if (switch_val == 0 ):



 			camera.start_preview()

			time.sleep(4)

			camera.capture('/home/pi/Desktop/capture.jpeg', resize=(320, 200))

			camera.stop_preview()

			if os.path.exists("textfile2.txt"):

				os.remove("textfile2.txt")

			else:

				print("File doesnt exist")



			time.sleep(2)

			os.system ('tesseract /home/pi/Desktop/capture.jpeg /home/pi/Desktop/textfile2 ')

			time.sleep(0.5)

			file = open("/home/pi/Desktop/textfile2.txt", "r")

			text1 = file.readline()

			text2 = file.readline()

			text3 = file.readline()

			file.close()

			text11=text1.lstrip()

			text22=text2.lstrip()

			text33=text3.lstrip()

			'''

			tab1=int(text11,2)

			tab2=int(text22,2)

			tab3=int(text33,2)

			'''

			tab1=(text11)

			tab2=(text22)

			tab3=(text33)

			print tab1

			print tab2

			print tab3

			time.sleep(3)

			

##########################

#DISPENSING OF TABLET1

##########################

			if (tab1=="100\n"):                                                                                                    

				if(hr==time1):

					print "Hi"

					tablet1_dispenser()

			elif(tab1=="111\n"):

				if(hr==time1):

					tablet1_dispenser()

			elif (tab1=="101\n"):

				if(hr==time1):

					tablet1_dispenser()

			elif (tab1=="110\n"):

				if(hr==time1):

					tablet1_dispenser()

			else:

				print "NO DISPENSING OF TABLET1"		



########################

#DISPENSING OF TABLET2

########################

			if (tab2=="010\n"):                                                                                                    

				if(hr==time2):

					print "Hi"

					tablet2_dispenser()

			elif(tab2=="111\n"):

				if(hr==time2):

					tablet2_dispenser()

			elif (tab2=="011\n"):

				if(hr==time2):

					tablet2_dispenser()

			elif (tab2=="110\n"):

				if(hr==time2):

					tablet2_dispenser()

			else:

				print "NO DISPENSING OF TABLET2"		

				

########################

#DISPENSING OF TABLET3

########################

			if (tab3=="011\n"):                                                                                                    

				if(hr==time3):

					print "Hi"

					tablet3_dispenser()

			elif(tab3=="111\n"):

				if(hr==time3):

					tablet3_dispenser()

			elif (tab3=="101\n"):

				if(hr==time3):

					tablet3_dispenser()

			elif (tab3=="001\n"):

				if(hr==time3):

					tablet3_dispenser()

			else:

				print "NO DISPENSING OF TABLET3"		

		

		else:

			GPIO.output(LED,GPIO.LOW)

			lcd.write8(0xC0)

			lcd.message('WAITING ..')

			print "waiting"

			time.sleep(0.5)	







except KeyboardInterrupt:

	GPIO.cleanup()

	camera.stop_preview()



