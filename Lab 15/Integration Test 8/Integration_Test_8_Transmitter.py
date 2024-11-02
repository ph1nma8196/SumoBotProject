# ECEN 2440
# Group 12
# Lab 15
# 11/2/2024

# Integration Test 8
# Testing IR Transmitter

import ir_tx
import time
import machine
from ir_tx.nec import NEC
from machine import Pin

tx_pin = Pin(9,Pin.OUT,value=0)
device_addr = 0x01
transmitter = NEC(tx_pin)

commands = [0x01,0x02,0x03,0x04]

if __name__ == "__main__":
  while True:
    for command in commands:
      transmitter.transmit(device_addr,command)
      print("COMMANDS",hex(command),"TRANSMITTED.")
      time.sleep(4)
