# ECEN 2440
# Group 12
# Lab 15
# 11/2/2024

# Integration Test 3
# Testing User LED

import time
import machine

led = machine.Pin(16,machine.Pin.OUT)

while True:
    led.high()
    time.sleep(1)
    led.low()
    time.sleep(1)