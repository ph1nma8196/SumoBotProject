# ECEN 2440
# Group 12
# Lab 15
# 11/2/2024

# Integration Test 4
# Testing Motor Driver
    
import machine
import math, time

from machine import PWM
from machine import Pin

time.sleep(1) # Wait 1 second

pwm_rate = 2000

# Pins Controlling Motor A
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)

# Pins Controlling Motor B
bin1_ph = Pin(10, Pin.OUT)
bin2_en = PWM(11, freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**17 * abs(1)), 0), 65535)

# Main loop to keep the script running
while True:
    time.sleep(1)

    # Motor A Moves Forward
    print("Motor A Forward")
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    # Motor B Moves Forward
    print("Motor B Forward")
    bin1_ph.low()
    bin2_en.duty_u16(pwm)

    # Run for 5 Seconds
    time.sleep(5)

    # Motor A Stops
    print("Motor A Stopped")
    ain1_ph.low()
    ain2_en.duty_u16(0)
    # Motor B Stops
    print("Motor B Stopped")
    bin1_ph.low()
    bin2_en.duty_u16(0)

    pass # Execution is interrupt-driven, so just keep the script alive