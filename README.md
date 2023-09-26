# Engineering_4_Notebook

&nbsp;




# Table of Contents
* [launchpad](#launchpad)
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Crash Avoidance](#Avoidance)

&nbsp;

# Avoidance

### Table of Contents

* [Avoidance1](#Avoidance1)
* [Avoidance2](#Avoidance2)


## Avoidance1

### Assignment Description

This assignment was the first of the crash avoidance siries. It introduced us to the MPU6050 Accelerometer and all we had to do was wire it up and have it print out the  X Y and Z values. 
### Evidence 

![gif](images/avoid1.gif)


### wiring diagram
 ![jpg](images/avoidwire1.jpg)

### Code
[code](raspberry-pi/avoid1.py).

### Reflection

This assignement introduce me to en entirely new system. The new MPU6050 Accelerometer/Gyro device was new but not difficult to understand and with the wiring for the project provided and the set up was easy. The code wsa a bit harder and required a new coding concept in this class, that being Arrays. This was not too difficult because i had covered them in other CS classes and the new syntax was pretty much the same (mpu.acceleration[0]). I just need to remeber to count from 0.   



## Avoidance2

### Assignment Description

This assignment was the second of the crash avoidance siries. It had us creat a battery powered system that turned on a warning light when it was turned more than 90 degrees 
### Evidence 

![gif](images/avoid2.gif)


### wiring diagram
 ![jpg](images/avoidwire1.jpg)

### Code
[code](raspberry-pi/avoid2.py).

### Reflection

this assignment was slightly more difficult, it added two new things for us to do; make a battery powered system and code a system that would turn on a led. The challennge for me was making sure the wiring was correct as the code only needed some if and elif (else if) statements, the wiring required me to use old things on this board like SCL and SDA but also some new things like the VSYS to power the board. Overall this project was still relatively easy but still required some trouble shooting of the LEDS and board to discover the flaws in my wiring and code. The biggest issue for me in this project was making sure that i was uploading code in the right way and that i was use LEDs that work. 












# launchpad
### Table of Contents
* [launchpad1](#launchpad1)
* [launchpad2](#launchpad2)
* [launchpad3](#launchpad3)
* [launchpad4](#launchpad4)

## launchpad1

### Assignment Description

This was a simple assignment that had us have a code output a countdown from 10 to 0 and say lift off at the end.
### Evidence 

![gif](images/launchpad1.gif)


### Code
[code](raspberry-pi/countdown.py).

### Reflection

This was an pretty easy assignment despite my lack of coding ability. The simple trick was making a for loop work in a range where it counted down, I my first iteration I had a for loop run ten times and and inside the for loop I put a simple subtraction and print method. For the later assignments i would change this to a more effiecent system of a for loop in a range of (10, 0, -1). I tried both for this assignment but desided on my first code because i understanded it better. Once i relaerned the syntax of the for loops this was a very achieveble assgnment. 



## launchpad2

### Assignment Description

this was the second in a siries of assignments about coding an countdown to launch for a pico board. This one added on the requierment to have a LED flash during the countdown and a different LED stay on after the countdown reached zero. 

### Evidence 

![gif](images/launchpad2.gif)

### wiring diagram
 ![jpg](images/launchwire2.jpg)

### Code
[code](raspberry-pi/launpad2.py).

### Reflection

this assignment made us have a light blink during the countdown, it was relatively easy as i only needed to modify the code before and add some LED code to make this work. As I was behind in work due to sickness it was nice that mason divers could help out with the LED setup code. The simple new thing to learn was ro figure out how to code the pins to the wires as the pico has new syntax. The saving grace was CNRL+P which allows you to open the pin map and then connect the right pins to the right places. Once that was acomplished the assignment was as easy as putting LED equal to true or false inside or out of the loop I had built in in the first assignment. 

## launchpad3

### Assignment Description

This was a assignment that had us have a code output a countdown from 10 to 0 after a button was pressed. 
### Evidence 

![gif](images/launchpad3.gif)

### wiring diagram
 ![jpg](images/launchwire3.jpg)

### Code
[code](raspberry-pi/launchpad3.py).

### Reflection

this little trick of coding was very simple, the wiring was about as simple as it comes but the code needed a while loop and to pull up the button but both proved easier than they first seemed. The button pull was the only difficult part as the wiring was extremely easy b/c the picos are more advanced than previous boards. The code needed a while loop to always check an if statement which is still realtively simple but requiered some trial and error. 

## launchpad4

### Assignment Description

this took all three of the last assignments and added them together. We had to have the button activate the countdown and the lights.
### Evidence 

![gif](images/launchpad4.gif)

### wiring diagram
 ![jpg](images/launchwire4.jpg)

### Code
[code](raspberry-pi/launchpad4.py).

### Reflection

the final launchpad assignment may have been the easiest as all i needed to do was copy and paste the code from the other ones. the challenge was making sure all the little complex things were in the right place and also repacing a broken button. The engineering challenge was largely just putting all of the stuff on one board and making sure all the wires, LEDs, resistors and the button were properly wired in. The code was just copy pasting the previos code together, and deciding whether or not they were inside the while loop.  






























## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;
