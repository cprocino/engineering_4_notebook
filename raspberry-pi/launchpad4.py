import time
import board  
import digitalio

print("countdown start now:")
counter = 10 
button = digitalio.DigitalInOut(board.GP16)   # butoon pin setup 
button.direction = digitalio.Direction.INPUT #button direction set up  
button.pull = digitalio.Pull.UP  # if the pin is up 


ledr = digitalio.DigitalInOut(board.GP14)  # led set ups 
ledy = digitalio.DigitalInOut(board.GP17)
ledy.direction = digitalio.Direction.OUTPUT # setting up thew direction 
ledr.direction = digitalio.Direction.OUTPUT # setting up thew direction

while True:  # loops 4ever
  if button.value == False:    # setting the button if statement
    for counter in range(10, 0, -1):  # setting up the for loop to run 10 times
        ledy.value = True # turning it on
        time.sleep(.25) # little time delay
        ledy.value = False  # turning it off
        time.sleep(.25) # little time delay
        print(counter)   # prining the value
    ledr.value = True # turning it on
    time.sleep(5) # little time delay
    ledr.value = False 



