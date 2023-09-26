# Import necessary libraries/modules
import board                    # Hardware pin mapping
import busio                    # Communication buses (e.g., I2C)
import digitalio                # Digital input/output pins
import time                     # Time-related functions
import adafruit_mpu6050         # Library for MPU6050 sensor
from adafruit_display_text import label  # Text display library
import adafruit_displayio_ssd1306       # OLED display library
import terminalio               # Terminal-style font
import displayio                # Display management

# Release any existing displays (if any)
displayio.release_displays()

# Define the SDA (data) and SCL (clock) pins for I2C communication
sda_pin = board.GP16
scl_pin = board.GP17

# Create an I2C object for communication
i2c = busio.I2C(scl_pin, sda_pin)

# Initialize an I2C display with a specific device address and reset pin
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)

# Create an SSD1306 OLED display object with specific width and height
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Initialize an MPU6050 sensor object for gyroscope and accelerometer data
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

# Define a digital output pin for signaling (e.g., an LED)
R = digitalio.DigitalInOut(board.GP1)

# Set the digital output pin to OUTPUT mode
R.direction = digitalio.Direction.OUTPUT

# Initialize a variable 'initial' with the current time and convert it to an integer
initial = time.monotonic()
initial = int(initial)

# Enter an infinite loop
while True:
    # Create a displayio Group to manage display content
    splash = displayio.Group()
    
    # Define a title for the display
    title = "ANGULAR VELOCITY"
    
    # Read X, Y, and Z angular velocity values from the MPU6050 sensor
    X = round(mpu.gyro[0], 3)
    Y = round(mpu.gyro[1], 3)
    Z = round(mpu.gyro[2], 3)
    
    # Create formatted strings for displaying angular velocity values
    x = f"X: {X} rad/s"
    y = f"Y: {Y} rad/s"
    z = f"Z: {Z} rad/s"
    
    # Create label objects for displaying text on the OLED screen
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    text_area2 = label.Label(terminalio.FONT, text=x, color=0xFFFF00, x=5, y=20)
    text_area3 = label.Label(terminalio.FONT, text=y, color=0xFFFF00, x=5, y=35)
    text_area4 = label.Label(terminalio.FONT, text=z, color=0xFFFF00, x=5, y=50)
    
    # Append label objects to the displayio Group
    splash.append(text_area)
    splash.append(text_area2)
    splash.append(text_area3)
    splash.append(text_area4)
    
    # Show the displayio Group on the OLED display
    display.show(splash)
    
    # Check if at least 1 second has passed since the last print operation
    if time.monotonic() - initial > 1:
        # Print X, Y, and Z acceleration values in meters per second squared
        print(f"X Acceleration: {mpu.acceleration[0]} m/s^2")
        print(f"Y Acceleration: {mpu.acceleration[1]} m/s^2")
        print(f"Z Acceleration: {mpu.acceleration[2]} m/s^2")
        print("")  # Print a blank line for formatting
        
        # Update the 'initial' time for the next print operation
        initial += 1
    
    # Check if X or Y acceleration is above 9.5 m/s^2 or below -9.5 m/s^2
    if mpu.acceleration[0] > 9.5 or mpu.acceleration[0] < -9.5:
        R.value = True  # Set the digital output pin to True
        
    # If X acceleration conditions are not met, check Y acceleration
    elif mpu.acceleration[1] > 9.5 or mpu.acceleration[1] < -9.5:
        R.value = True  # Set the digital output pin to True
        
    else:
        R.value = False  # Set the digital output pin to False
