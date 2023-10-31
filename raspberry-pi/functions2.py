# Import necessary libraries and modules
import board
import busio
from adafruit_display_text import label
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import adafruit_displayio_ssd1306
import terminalio
import displayio

# Define a function 'tri' to calculate the area of a triangle given its coordinates.
def tri(x1, y1, x2, y2, x3, y3):
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return area

# Release any existing displays (if any)
displayio.release_displays()

# Define the SDA (data) and SCL (clock) pins for I2C communication
sda_pin = board.GP14
scl_pin = board.GP17

# Create an I2C object for communication
c = busio.I2C(scl_pin, sda_pin)

# Initialize an I2C display with a specific device address and reset pin
display_bus = displayio.I2CDisplay(c, device_address=0x3d, reset=board.GP0)

# Create an SSD1306 OLED display object with specific width and height
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Initialize an MPU6050 sensor object for gyroscope and accelerometer data
mpu = adafruit_mpu6050.MPU6050(c, address=0x68)

# Define a digital output pin for signaling (e.g., an LED)
R = digitalio.DigitalInOut(board.GP1)

# Set the digital output pin to OUTPUT mode
R.direction = digitalio.Direction.OUTPUT

# Initialize a variable 'initial' with the current time and convert it to an integer
initial = time.monotonic()
initial = int(initial)

# Enter an infinite loop
while True:
    # Prompt the user to enter the first set of coordinates in x,y format
    print("Enter the first coordinates in x,y:")
    one = input()
    one = one.split(",")
    x1 = int(one[0])
    y1 = int(one[1])

    # Prompt the user to enter the second set of coordinates in x,y format
    print("Enter the second coordinates in x,y:")
    two = input()
    two = two.split(",")
    x2 = int(two[0])
    y2 = int(two[1])

    # Prompt the user to enter the third set of coordinates in x,y format
    print("Enter the third coordinates in x,y:")
    third = input()
    third = third.split(",")
    x3 = int(third[0])
    y3 = int(third[1])

    # Calculate the area of the triangle using the 'tri' function
    var = tri(x1, y1, x2, y2, x3, y3)

    # Display the calculated area of the triangle
    print("The area is:")
    print(var)

    # Create a displayio Group to manage display content
    splash = displayio.Group()
    title = f"{var}km^2"  # Display the area of the triangle at the top

    # Create a label for displaying text on the OLED screen
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)

    # Create graphical shapes for display
    hline = Line(0, 32, 128, 32, color=0xFFFF00)  # Horizontal line
    vline = Line(64, 0, 64, 64, color=0xFFFF00)   # Vertical line
    circle = Circle(64, 32, 2, outline=0xFFFF00)   # Circle in the center
    triangle = Triangle(x1 + 64, 32 - y1, x2 + 64, 32 - y2, x3 + 64, 32 - y3, outline=0xFFFF00)

    # Append the graphical elements to the displayio Group
    splash.append(triangle)
    splash.append(circle)
    splash.append(hline)
    splash.append(vline)
    splash.append(text_area)

    # Show the displayio Group on the OLED display
    display.show(splash)