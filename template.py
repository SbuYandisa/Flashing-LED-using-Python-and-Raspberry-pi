#!/usr/bin/python3
"""
Python Practical Template
Name: Yandisa Madinga
Student Number: MDNYAN002
Prac: Prac 1
Date: 29/07/2019
"""

import RPi.GPIO as GPIO
import time
import itertools

listIndex=0
channel_list=(7,13,15)
binary_list =list()
#configure GPIOs
def initGPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
#------------------------------------------------------------------------------------
#initialise LEDs and configure GPIOs
def initLED():
    GPIO.setup(7,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(13,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(15,GPIO.OUT, initial=GPIO.LOW)
#-------------------------------------------------------------------------------------
#initialise buttons and configure GPIOs
def initBTNS():
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#--------------------------------------------------------------------------------------
#binary number generator function
def BinaryConversion():
    list = []
    for x in map(' '.join, itertools.product('01', repeat=3)):
        list.append(x)
    return list
#---------------------------------------------------------------------------------------
#converts binary list to binary integer list
def listOfNum():
    num_list = []
    for item in BinaryConversion():
        bNum=item.split(" ")
        results = [int(i) for i in bNum]
        num_list.append(results)
    return num_list
#-----------------------------------------------------------------------------------------
#flash LEDs function responding to button at pin16
def increment(e):
    global binary_list
    global listIndex
    listNum = listOfNum()
    listIndex +=1
    if listIndex >= len(listNum):
        listIndex=0
    binary_list=listNum[listIndex]
    print(binary_list)
    GPIO.output(channel_list,binary_list)
#----------------------------------------------------------------------------------------
#flash LEDs function responding to button at pin11
def decrement(e):
    global binary_list
    global listIndex
    listNum = listOfNum()
    listIndex -=1
    if listIndex == 0:
        listIndex=len(listNum) - 1
    binary_list=listNum[listIndex]
    print(binary_list)
    GPIO.output(channel_list,binary_list)
#listens to a pressed button using interrupts
def btnChecker():
    GPIO.add_event_detect(16, GPIO.FALLING, callback=increment, bouncetime=300)
    GPIO.add_event_detect(11, GPIO.FALLING, callback=decrement, bouncetime=300)
#-------------------------------------------------------------------------------------
def main():
    pass
if __name__== '__main__':
    try:
        initGPIO()
        initBTNS()
        initLED()
        btnChecker()
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting grcefully")
        # Turn off GPIOs 
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occured")
        print(e.message)
