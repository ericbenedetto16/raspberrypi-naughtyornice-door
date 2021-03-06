from time import sleep
from random import randint
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO Pin Numbers
green=33
red=32
button=7
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

buttonPressed=False

#Initliaize pygame sounds
pygame.init()
pygame.mixer.music.set_volume(1.0)

while(1):
    try:
        if GPIO.input(button)==0:
            print "button pressed"
            #Rand number
            buttonPressed=True
            rand=randint(0,1000)
            print rand
            if (rand%2)==0:
                pygame.mixer.music.load("santababy.mp3")
                pygame.mixer.music.play()
                #Light Up green
                GPIO.output(green,True)
                sleep(15)
                #Play nice song
                GPIO.output(green,False)
                pygame.mixer.music.stop()
                buttonPressed=False
            else:
                pygame.mixer.music.load("highway.mp3")
                pygame.mixer.music.play()
                #Light Up red
                GPIO.output(red,True)
                sleep(15)
                GPIO.output(red,False)
                pygame.mixer.music.stop()
                buttonPressed=False
    except KeyboardInterrupt:
        GPIO.output(green,False)
        GPIO.output(red,False)
        GPIO.cleanup()
        exit()
