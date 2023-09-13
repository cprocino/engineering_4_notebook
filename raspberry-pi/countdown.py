# count down code 
import time
import board  
print("countdown start now:")
int counter = 10 

for counter in range(10):
  time.sleep(.5)
  print(counter)
  counter = counter - 1 

