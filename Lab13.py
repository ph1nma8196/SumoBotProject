# ECEN 2440
# Group 12
# Lab 13
# 10/24/2024
    
import ir_rx

import machine
import math, time

from machine import PWM
from machine import Pin

from machine import Pin
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging

time.sleep(1)

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)

bin1_ph = Pin(10, Pin.OUT)
bin2_en = PWM(11, freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**17 * abs(1)), 0), 65535)

# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
    if (data == 1):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

        print("Motor A Forward")
        ain1_ph.low()
        ain2_en.duty_u16(pwm)
        time.sleep(1)

        print("Motor B Forward")
        bin1_ph.low()
        bin2_en.duty_u16(pwm)
        time.sleep(1)

    elif (data == 2):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

        print("Motor A Stopped")
        ain1_ph.low()
        ain2_en.duty_u16(0)
        time.sleep(1)

        print("Motor B Stopped")
        bin1_ph.low()
        bin2_en.duty_u16(0)
        time.sleep(1)

    elif (data == 3):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

        print("Motor A Reverse")
        ain1_ph.high()
        ain2_en.duty_u16(pwm)
        time.sleep(1)

        print("Motor B Reverse")
        bin1_ph.high()
        bin2_en.duty_u16(pwm)
        time.sleep(1)

    elif (data == 4):
        print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

        print("Motor A Stopped")
        ain1_ph.low()
        ain2_en.duty_u16(0)
        time.sleep(1)

        print("Motor B Stopped")
        bin1_ph.low()
        bin2_en.duty_u16(0)
        time.sleep(1)

# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)

# Main loop to keep the script running
while True:
    pass # Execution is interrupt-driven, so just keep the script alive
