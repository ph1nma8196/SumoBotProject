# ECEN 2440
# Group 12
# Lab 15
# 11/2/2024

# Integration Test 7
# Testing IR Receiver with Motors
    
import ir_rx

import machine
import math, time

from machine import PWM
from machine import Pin

from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging

time.sleep(1) # Wait 1 second

pwm_rate = 2000

# Pins Controlling Motor A
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)

# Pins Controlling Motor B
bin1_ph = Pin(10, Pin.OUT)
bin2_en = PWM(11, freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**17 * abs(1)), 0), 65535)

# User LED
LED = Pin(18, Pin.OUT)

# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):

    # Four data values, 1-4, transmitted from IR transmitter

    if (data == 1):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
        LED.high()

        # Motor A Moves Forward
        print("Motor A Forward")
        ain1_ph.low()
        ain2_en.duty_u16(pwm)

        time.sleep(1)
        LED.low()

        # Motor B Moves Forward
        print("Motor B Forward")
        bin1_ph.low()
        bin2_en.duty_u16(pwm)

    elif (data == 2):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
        LED.high()
        
        # Motor A Stops
        print("Motor A Stopped")
        ain1_ph.low()
        ain2_en.duty_u16(0)

        time.sleep(1)
        LED.low()

        # Motor B Stops
        print("Motor B Stopped")
        bin1_ph.low()
        bin2_en.duty_u16(0)

    elif (data == 3):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
        LED.high()

        # Motor A Reverses
        print("Motor A Reverse")
        ain1_ph.high()
        ain2_en.duty_u16(pwm)

        time.sleep(1)
        LED.low()

        # Motor B Reverses
        print("Motor B Reverse")
        bin1_ph.high()
        bin2_en.duty_u16(pwm)

    elif (data == 4):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")
        LED.high()

        # Motor A Stops
        print("Motor A Stopped")
        ain1_ph.low()
        ain2_en.duty_u16(0)

        time.sleep(1)
        LED.low()

        # Motor B Stops
        print("Motor B Stopped")
        bin1_ph.low()
        bin2_en.duty_u16(0)

# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)

# Main loop to keep the script running
while True:
    pass # Execution is interrupt-driven, so just keep the script alive