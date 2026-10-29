import board
import digitalio
import time

# Set up onboard LED as output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Set up button on GP15 as input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Control LED with button
while True:
    if button.value == False: #button pressed
        led.value = True #on
    else:
        led.value = False #off

    time.sleep(0.01)

