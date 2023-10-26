import board
import busio
import digitalio
import adafruit_mpu6050
from adafruit_display_shapes.triangle import Triangle
import adafruit_displayio_ssd1306
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

import terminalio
import displayio



def tri(x1, y1, x2, y2, x3, y3):
        area = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2
        return area

while True:
        print (" first cordinates in x,y:")
        one = input()
        one = one.split(",")
        x1 = (int(one[0]))
        y1 = (int(one[1]))
        print (" second cordinates in x,y:")
        two = input()
        two = two.split(",")
        x2 = (int(two[0]))
        y2 = (int(two[1]))
        print (" third cordinates in x,y:")
        third = input()
        third =third.split(",")
        x3 = (int(third[0]))
        y3 = (int(third [1]))
        var = tri(x1, y1, x2, y2, x3, y3)
        print (f"the area is:" )
        print (var)

