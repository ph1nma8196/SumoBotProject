# ECEN 2440
# Group 12
# 12/12/2024

from machine import Pin
import time

# Define the pin connected to the QRE1113 sensor
Reflector_Pin_Left = Pin(16, Pin.OUT)  # GPIO 16 on the Raspberry Pi Pico
Reflector_Pin_Right = Pin(17, Pin.OUT)  # GPIO 16 on the Raspberry Pi Pico


def readSensor(Reflector_Pin):
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
    sensor_value_left = readSensor(Reflector_Pin_Left)
    sensor_value_right = readSensor(Reflector_Pin_Right)
    
    # Print the sensor value to the console
    print("16 ", sensor_value_left)
    print("17 ", sensor_value_right)
    
    # Delay to make the output readable
    time.sleep(0.1)  # 100 ms delay
