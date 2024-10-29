import machine
from machine import I2C, Pin
import seesaw
import time
import seesaw

# Initialize I2C. Adjust pin numbers based on your Pico's configuration
i2c = I2C(0, scl=Pin(17), sda=Pin(16))

# Initialize the Seesaw driver with the I2C interface
# Use the Gamepad QT's I2C address from the Arduino code (0x50)
seesaw_device = seesaw.Seesaw(i2c, addr=0x50)

# Define button and joystick pin numbers as per the Arduino code
BUTTON_A = 5
BUTTON_B = 1
BUTTON_X = 6
BUTTON_Y = 2
BUTTON_START = 16
BUTTON_SELECT = 0
JOYSTICK_X_PIN = 15
JOYSTICK_Y_PIN = 14

# Button mask based on Arduino code
BUTTONS_MASK = (1 << BUTTON_X) | (1 << BUTTON_Y) | \
              (1 << BUTTON_A) | (1 << BUTTON_B) | \
              (1 << BUTTON_SELECT) | (1 << BUTTON_START)

# Define LED pins
LED_1_PIN = 12
LED_2_PIN = 13
LED_3_PIN = 15
LED_4_PIN = 14

# Motor control pins
MOTOR_LEFT_PIN = Pin(2, Pin.OUT)
MOTOR_RIGHT_PIN = Pin(3, Pin.OUT)

# IR receiver setup (adjust pin)
IR_PIN = Pin(4, Pin.IN)

# Initialize LED states
led_states = {
   BUTTON_A: False,
   BUTTON_B: False,
   BUTTON_X: False,
   BUTTON_Y: False,
   BUTTON_START: False,
   BUTTON_SELECT: False
}

# Initialize joystick center position
joystick_center_x = 511
joystick_center_y = 497

# Joystick movement thresholds
joystick_threshold = 50

def setup_buttons():
   """Configure the pin modes for buttons."""
   seesaw_device.pin_mode_bulk(BUTTONS_MASK, seesaw_device.INPUT_PULLUP)

def read_buttons():
   """Read and return the state of each button."""
   return seesaw_device.digital_read_bulk(BUTTONS_MASK)

def set_led(pin, state):
   """Turn the LED connected to the given pin on or off."""
   pin.value(state)

def handle_button_press(button):
   """Toggle the corresponding LED state on button press."""
   global led_states
   led_states[button] = not led_states[button]
   if button == BUTTON_A:
       set_led(Pin(LED_1_PIN, Pin.OUT), led_states[button])
   elif button == BUTTON_B:
       set_led(Pin(LED_2_PIN, Pin.OUT), led_states[button])
   elif button == BUTTON_X:
       set_led(Pin(LED_3_PIN, Pin.OUT), led_states[button])
   elif button == BUTTON_Y:
       set_led(Pin(LED_4_PIN, Pin.OUT), led_states[button])
   print("Button", button, "is", "pressed" if led_states[button] else "released")

def control_motors(direction):
   """Control motor pins based on joystick direction."""
   if direction == 'forward':
       MOTOR_LEFT_PIN.value(1)
       MOTOR_RIGHT_PIN.value(1)
   elif direction == 'backward':
       MOTOR_LEFT_PIN.value(0)
       MOTOR_RIGHT_PIN.value(0)
   elif direction == 'left':
       MOTOR_LEFT_PIN.value(0)
       MOTOR_RIGHT_PIN.value(1)
   elif direction == 'right':
       MOTOR_LEFT_PIN.value(1)
       MOTOR_RIGHT_PIN.value(0)
   else:
       MOTOR_LEFT_PIN.value(0)
       MOTOR_RIGHT_PIN.value(0)

def main():
   """Main program loop."""
   setup_buttons()
   last_buttons = 0

   last_x, last_y = seesaw_device.analog_read(JOYSTICK_X_PIN), seesaw_device.analog_read(JOYSTICK_Y_PIN)

   while True:
       current_buttons = read_buttons()

       # Check if button state has changed
       for button in led_states:
           if current_buttons & (1 << button) and not last_buttons & (1 << button):
               handle_button_press(button)

       # Read joystick values
       current_x = seesaw_device.analog_read(JOYSTICK_X_PIN)
       current_y = seesaw_device.analog_read(JOYSTICK_Y_PIN)

       # Determine bot movement based on joystick
       if current_y < joystick_center_y - joystick_threshold:
           print("Moving forward")
           control_motors('forward')
       elif current_y > joystick_center_y + joystick_threshold:
           print("Moving backward")
           control_motors('backward')
       elif current_x < joystick_center_x - joystick_threshold:
           print("Turning left")
           control_motors('left')
       elif current_x > joystick_center_x + joystick_threshold:
           print("Turning right")
           control_motors('right')
       else:
           control_motors('stop')

       last_buttons = current_buttons
       time.sleep(0.1)  # Delay to prevent overwhelming the output

if __name__ == "__main__":
   main()
