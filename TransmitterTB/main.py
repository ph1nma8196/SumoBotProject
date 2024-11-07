import ir_tx
import time
import machine
from ir_tx.nec import NEC
from machine import Pin

tx_pin = Pin(9,Pin.OUT,value=0)
device_addr = 0xFF
transmitter = NEC(tx_pin)

commands = [100,200,10,20]

if __name__ == "__main__":
  while True:
    for command in commands:
      transmitter.transmit(device_addr,command)
      print("COMMANDS",hex(command),"TRANSMITTED.")
      time.sleep(4)
