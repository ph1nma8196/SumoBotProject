# ECEN 2440
# Group 12
# Lab 13
# 11/14/2024
    
import ir_rx

import machine
import math, time

from machine import PWM
from machine import Pin

from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging



time.sleep(1) # Wait 1 second

pwm_rate = 2000

d0 = Pin(7, Pin.IN)
d1 = Pin(6, Pin.IN)
d2 = Pin(5, Pin.IN)
d3 = Pin(4, Pin.IN)

# Pins Controlling Motor A
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)

# Pins Controlling Motor B
bin1_ph = Pin(10, Pin.OUT)
bin2_en = PWM(11, freq = pwm_rate, duty_u16 = 0)

pwm = min(max(int(2**17 * abs(1)), 0), 65535)

current_x = 0
current_y = 0

# Callback function to execute when an IR code is received
def ir_callback(data, addr, _):
    print(f"Position Recieved. X: {data}, Y: {addr}")
    #time.sleep(0.3)
    if(addr==8): # Here, use tank controls
        pwmPercent = 0
        print("MOTORS OFF")
    elif(addr<8): #otherwise, use smooth steering controls.
        pwmPercent = (1/(addr+1))
        ain1_ph.low()
        bin1_ph.high()
        print("REVERSE, ", pwmPercent)
    else:
        pwmPercent = ((addr-8)/8)
        ain1_ph.high()
        bin1_ph.low()
        print("FORWARDS, ", pwmPercent)
    if(data==8):
        ain2_en.duty_u16(int(pwm*pwmPercent))
        bin2_en.duty_u16(int(pwm*pwmPercent))
        print("STRAIGHT")
    elif(data<8):
        ain2_en.duty_u16(int(pwm*(1/pwmPercent)))
        bin2_en.duty_u16(int(pwm*(pwmPercent))) #ON
        print("MOTOR A FORWARDS MOTOR B ADJUSTED")
    else:
        ain2_en.duty_u16(int(pwm*(pwmPercent))) #ON
        bin2_en.duty_u16(int(pwm*(1/pwmPercent)))
        print("MOTOR B FORWARDS MOTOR A ADJUSTED")

        

        

# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the pin number based on your wiring

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

# Optional: Use the print_error function for debugging
ir_receiver.error_function(print_error)

# Main loop to keep the script running
while True:
    if (d3.value() == 1):

        # Motor A Moves Forward
        print("Motor A Forward")
        ain1_ph.low()
        ain2_en.duty_u16(pwm)

        # Motor B Moves Forward
        print("Motor B Forward")
        bin1_ph.low()
        bin2_en.duty_u16(pwm)

        time.sleep(0.35)

        if (d3.value() == 0):
            # Motor A Stops
            print("Motor A Stopped")
            ain1_ph.low()
            ain2_en.duty_u16(0)

            # Motor B Stops
            print("Motor B Stopped")
            bin1_ph.low()
            bin2_en.duty_u16(0)

    elif (d2.value() == 1):
        
        # Motor A Reverses
        print("Motor A Reverse")
        ain1_ph.high()
        ain2_en.duty_u16(pwm)

        # Motor B Reverses
        print("Motor B Reverse")
        bin1_ph.high()
        bin2_en.duty_u16(pwm)

        time.sleep(0.35)

        if (d2.value() == 0):
            # Motor A Stops
            print("Motor A Stopped")
            ain1_ph.low()
            ain2_en.duty_u16(0)

            # Motor B Stops
            print("Motor B Stopped")
            bin1_ph.low()
            bin2_en.duty_u16(0)

    elif (d1.value() == 1):

        # Motor A Stops
        print("Motor A Stopped")
        ain1_ph.low()
        ain2_en.duty_u16(0)

        # Motor B Moves Forward
        print("Motor B Forward")
        bin1_ph.low()
        bin2_en.duty_u16(pwm)

        time.sleep(0.15)

        if (d1.value() == 0):
            # Motor A Stops
            print("Motor A Stopped")
            ain1_ph.low()
            ain2_en.duty_u16(0)

            # Motor B Stops
            print("Motor B Stopped")
            bin1_ph.low()
            bin2_en.duty_u16(0)

    elif (d0.value() == 1):

        # Motor A Moves Forward
        print("Motor A Forward")
        ain1_ph.low()
        ain2_en.duty_u16(pwm)

        # Motor B Stops
        print("Motor B Stopped")
        bin1_ph.low()
        bin2_en.duty_u16(0)

        time.sleep(0.15)

        if (d0.value() == 0):
            # Motor A Stops
            print("Motor A Stopped")
            ain1_ph.low()
            ain2_en.duty_u16(0)

            # Motor B Stops
            print("Motor B Stopped")
            bin1_ph.low()
            bin2_en.duty_u16(0)

    pass # Execution is interrupt-driven, so just keep the script alive
