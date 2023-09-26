import time
import board # importing the board and and all the nessecary starting bits
import digitalio
import adafruit_mpu6050
import busio

sda_pin = board.GP14 #
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)  # mpu var

led = digitalio.DigitalInOut(board.GP1)   #pico pin 
led.direction = digitalio.Direction.OUTPUT    # output pin 
led.value = True
while True:
    print(f"Y: {mpu.acceleration[1]} m/s^2")   #prints the y values
    if mpu.acceleration[0] > 8 or mpu.acceleration[0] < -8:   #if x direction
        led.value = True                                              #led  on
    elif mpu.acceleration[1] > 8 or mpu.acceleration[1] < -8:     #if y direction
        led.value = True
    else:
        led.value = False
    time.sleep(.1)
