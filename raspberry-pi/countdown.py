# count down code 
import time
import board  
print("countdown start now:")
int counter = 10 

for counter in range(10):  # setting up the for loop to run 10 times
  time.sleep(.5) # little time delay
  print(counter)   # prining the value 
  counter = counter - 1  # doing the counting down

