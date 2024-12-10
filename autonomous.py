from machine import Pin, PWM
import time

# define sensor and motor control
Reflector_Pin = Pin(20, Pin.OUT) 
ain1_ph = Pin(12, Pin.OUT)  # motor A direction
ain2_en = PWM(Pin(13), freq=2000, duty_u16=0)  # motor A PWM
bin1_ph = Pin(14, Pin.OUT)  # Motor B direction
bin2_en = PWM(Pin(15), freq=2000, duty_u16=0)  # motor B PWM

# constants
PWM_MAX = 65535  # max duty cycle
FORWARD_THRESHOLD_LOW = 1000
FORWARD_THRESHOLD_HIGH = 2500

def readSensor():
    Reflector_Pin.init(Pin.OUT)
    Reflector_Pin.value(1)
    time.sleep_us(10)  # 10 microsecond delay
    Reflector_Pin.init(Pin.IN)
    start_time = time.ticks_us()
    while Reflector_Pin.value() == 1 and time.ticks_diff(time.ticks_us(), start_time) < 10000:
        pass
    return time.ticks_diff(time.ticks_us(), start_time)

def stop_motors():
    ain1_ph.low()
    ain2_en.duty_u16(0)
    bin1_ph.low()
    bin2_en.duty_u16(0)
def move_forward():
    ain1_ph.low()
    ain2_en.duty_u16(PWM_MAX // 2)  # adjust speed 
    bin1_ph.high()
    bin2_en.duty_u16(PWM_MAX // 2)

while True:
    sensor_value = readSensor()
    print(f"Sensor Value: {sensor_value}")
    
    if FORWARD_THRESHOLD_LOW <= sensor_value < FORWARD_THRESHOLD_HIGH:
        print("Detected threshold. Moving forward.")
        move_forward()
    else:
        print("No detection. Stopping.")
        stop_motors()
    
    time.sleep(0.1)  # delay

