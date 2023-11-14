# Ignore type checking for this script
# This is useful for cases where type hints might not be fully supported or causing issues
# The `# type: ignore` comment tells the type checker to ignore the type hinting in this file
# It's typically used in scenarios where the code is more dynamic or interacts with hardware

# Import necessary libraries and modules
import board
import busio
import adafruit_mpu6050
import digitalio
import time
import storage

# Define the pin for the built-in LED
led_pin = board.LED  
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

# Define the pin for an additional LED (led_2)
led_2_pin = board.GP16  
led_2 = digitalio.DigitalInOut(led_2_pin)
led_2.direction = digitalio.Direction.OUTPUT

# Define pins for I2C communication
sda_pin = board.GP14 
scl_pin = board.GP15  
i2c = busio.I2C(scl_pin, sda_pin)

# Initialize MPU6050 sensor object for gyroscope and accelerometer data
mpu = adafruit_mpu6050.MPU6050(i2c)

# Function to check if the device is tilted based on acceleration data
def is_tilted(acceleration, tilt_threshold):
    x_acceleration, y_acceleration, z_acceleration = acceleration
    return z_acceleration < -tilt_threshold

# Open or create a CSV file for data logging
with open("/data.csv", "a") as datalog:
    while True:
        time_elapsed = time.monotonic()

        acceleration = mpu.acceleration
        x_acceleration, y_acceleration, z_acceleration = acceleration

        tilt_threshold = 0.45  # Threshold for considering the device tilted
        tilt = 1 if is_tilted(acceleration, tilt_threshold) else 0

        # Control the state of led_2 based on z_acceleration
        if z_acceleration < -tilt_threshold:
            led_2.value = True
        else:
            led_2.value = False

        # Format data and write it to the CSV file
        data_string = f"{time_elapsed:.2f},{x_acceleration:.3f},{y_acceleration:.3f},{z_acceleration:.3f},{tilt}\n"
        datalog.write(data_string)

        # Blink the built-in LED
        led.value = True
        time.sleep(0.1)
        led.value = False

        datalog.flush()  # Flush the buffer to ensure data is written to the file

        time.sleep(0.25)  # Pause to control the loop speed
