#Imports
from time import sleep
from random import randint
import pygame
import RPi.GPIO as GPIO

#GPIO Pin Initialization
GPIO.setmode(GPIO.BOARD)
#Physical Pin Numbers
green=33
red=32
button=7
#Setup Input/Output Pins
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#Boolean For Button Press
buttonPressed=False

#Initliaize pygame sounds
pygame.init()
pygame.mixer.music.set_volume(1.0)


#Main Loop
while(1):
    #Try Statement to Catch KeyboardInterrupt and Cleanup
    try:
        #If Button Pressed
        if GPIO.input(button)==0:
            #Stop Generic Music
            pygame.mixer.music.stop()
            #Turn off Lights
            GPIO.output(green,False)
            GPIO.output(red,False)
            #Debugging
            print "button pressed"
            #User Interface Delay
            sleep(0.7)
            #Rand number
            rand=randint(0,1000)
            #Debugging
            print rand
            #If Even Number...Call Nice Statements
            if (rand%2)==0:
                #Play Santa Baby Snippet
                pygame.mixer.music.load("santababy.mp3")
                pygame.mixer.music.play()
                #Light Up Green for 15 Seconds
                GPIO.output(green,True)
                sleep(15)
                #Turn off Lights, Stop Music, Reset Boolean
                GPIO.output(green,False)
                pygame.mixer.music.stop()
                buttonPressed=False
                #User Interface Delay
                sleep(1.3)
            #If Odd Number..Call Naughty Statements
            else:
                #Play Highway to Hell Snippet
                pygame.mixer.music.load("highway.mp3")
                pygame.mixer.music.play()
                #Light Up red for 15 Seconds
                GPIO.output(red,True)
                sleep(15)
                #Turn off Lights, Stop Music, Reset Boolean
                GPIO.output(red,False)
                pygame.mixer.music.stop()
                buttonPressed=False
                #User Interface Delay
                sleep(1.3)
        #If Button Is Not Pressed
        else:
            #Get Random Song To Play
            musicIndex = randint(1,5)
            if musicIndex==1:
                pygame.mixer.music.load("jinglebells.mp3")
            if musicIndex==2:
                pygame.mixer.music.load("letitsnow.mp3")
            if musicIndex==3:
                pygame.mixer.music.load("mostwonderfultime.mp3")
            if musicIndex==4:
                pygame.mixer.music.load("grinch.mp3")
            if musicIndex==5:
                pygame.mixer.music.load("deckthehalls.mp3")
            #Loop Song Infinitely
            pygame.mixer.music.play(-1)
            #While the Button is Not Pressed
            while GPIO.input(button)!=0:
                #Turn on Both LED Strips
                GPIO.output(green,True)
                GPIO.output(red,True)
    #If ^C
    except KeyboardInterrupt:
        #Turn off Lights
        GPIO.output(green,False)
        GPIO.output(red,False)
        #Cleanup Pins
        GPIO.cleanup()
        #Exit Script
        exit()
