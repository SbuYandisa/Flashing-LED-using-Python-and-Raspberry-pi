import RPi.GPIO as GPIO
import time

#configure GPIOs
def initGPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
#initialise LEDs and configure GPIOs
def initLED():
    GPIO.setup(7,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(13,GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(15,GPIO.OUT, initial=GPIO.LOW)

#initialise buttons and configure GPIOs
def initBTNS():
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#flash LEDs function
def flashLEDs():
    while True:
        Button = GPIO.input(11)
        if Button ==False:
            GPIO.output(7,False)
            GPIO.output(13,False)
            GPIO.output(15,False)
            print("Running............")
        else:
            GPIO.output(7,True)
            GPIO.output(13,True)
            GPIO.output(15,True)
            print("Running...........")
def main():
    initGPIO()
    initLED()
    initBTNS()
    GPIO.add_event_detect(11, GPIO.RISING, flashLEDs())
if __name__== '__main__':
    main()
