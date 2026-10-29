import board
import digitalio
import time

# Set up the onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Blink the LED forever
while True:
    led.value = True #on
    time.sleep(0.5) #time interval

    led.value = False #off
    time.sleep(0.5) #time interval

