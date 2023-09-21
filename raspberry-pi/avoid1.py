import time
import board # importing the board and and all the nessecary starting bits
import digitalio
import adafruit_mpu6050
import busio

sda_pin = board.GP14   # setting up the pin for SDA
scl_pin = board.GP15   #  setting up the pin for Scl
i2c = busio.I2C(scl_pin, sda_pin)    # setting up the i2c var
mpu = adafruit_mpu6050.MPU6050(i2c)  # setting up the mpu var


while True:
    print(f"X: {mpu.acceleration[0]} m/s^2")   #prints the x values
    print(f"Y: {mpu.acceleration[1]} m/s^2")   #prints the y values
    print(f"Z: {mpu.acceleration[2]} m/s^2")  #prints the z values
    time.sleep(1)
    print()
