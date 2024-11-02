import time
import machine

d0 = machine.Pin(7,machine.Pin.IN)
d1 = machine.Pin(6,machine.Pin.IN)
d2 = machine.Pin(5,machine.Pin.IN)
d3 = machine.Pin(4,machine.Pin.IN)
led = machine.Pin(18,machine.Pin.OUT)

while True:
    if(d0.value() == 1):
        led.high()
    elif(d1.value() == 1):
        led.high()
    elif(d2.value() == 1):
        led.high()
    elif(d3.value() == 1):
        led.high()
    else:
        led.low()
    time.sleep(.1)
