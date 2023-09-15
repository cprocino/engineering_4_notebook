# count down code with lights 
import time
import board  
import digitalio

print("countdown start now:")
counter = 10 
ledr = digitalio.DigitalInOut(board.GP14)
ledy = digitalio.DigitalInOut(board.GP16)
ledy.direction = digitalio.Direction.OUTPUT # setting up thew direction 
ledr.direction = digitalio.Direction.OUTPUT # setting up thew direction 

for counter in range(10, 0, -1):  # setting up the for loop to run 10 times
  ledy.value = True
  time.sleep(.25) # little time delay
  ledy.value = False
  time.sleep(.25) # little time delay
  print(counter)   # prining the value

ledr.value=True
time.sleep(5)

