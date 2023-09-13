# type: ignore 

import time
import board # importing the board and and all the nessecary starting bits
import digitalio

led = digitalio.DigitalInOut(board.LED)  # setting up the LEDs 
led.direction = digitalio.Direction.OUTPUT # setting up thew direction 
while True:   # loop
    led.value = True 
    time.sleep(.5)
    led.value = False 
    time.sleep(.5)
