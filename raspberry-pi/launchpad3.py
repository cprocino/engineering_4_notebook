import time
import board  
import digitalio

print("countdown start now:")
counter = 10 
button = digitalio.DigitalInOut(board.GP16)   # butoon pin setup 

button.pull = digitalio.Pull.UP  # if the pin is up 

while True:  # loops 4ever
  if button.value == False:    # setting the button if statement
    for counter in range(10, 0, -1):  # setting up the for loop to run 10 times
        time.sleep(.5) # little time delay
        print(counter)   # prining the value



