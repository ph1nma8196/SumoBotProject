# ECEN 2440
# Group 12
# 11/12/2024

from machine import Pin
import time

# Define the pin connected to the QRE1113 sensor
Reflector_Pin = Pin(20, Pin.OUT)  # GPIO 2 on the Raspberry Pi Pico
Blue = Pin(12, Pin.OUT)
Green = Pin(13, Pin.OUT)
Yellow = Pin(14, Pin.OUT)
Red = Pin(15, Pin.OUT)


def readSensor():
    # Set the pin as output and write HIGH
    Reflector_Pin.init(Pin.OUT)
    Reflector_Pin.value(1)
    time.sleep_us(10)  # Wait 10 microseconds
    
    # Set the pin as input to measure response time
    Reflector_Pin.init(Pin.IN)
    
    # Get the current time in microseconds
    start_time = time.ticks_us()
    
    # Measure how long the pin stays HIGH, max 3000 us
    while Reflector_Pin.value() == 1 and time.ticks_diff(time.ticks_us(), start_time) < 10000:
        pass
    
    # Calculate the time difference
    difference = time.ticks_diff(time.ticks_us(), start_time)
    return difference

while True:
    # Read the QRE1113 sensor value
    sensor_value = readSensor()
    
    # Print the sensor value to the console
    print(sensor_value)

    if (sensor_value < 7500 & sensor_value >= 5000):
        Red.low()
        Yellow.high()
    elif (sensor_value < 5000 & sensor_value >= 2500):
        Red.low()
        Green.high()
    elif (sensor_value < 2500):
        Red.low()
        Blue.high()
    else:
        Blue.low()
        Green.low()
        Yellow.low()
        Red.high()
    
    # Delay to make the output readable
    time.sleep(0.1)  # 100 ms delay
