# Blink with variable

#  Turn an LED on for one sec, then off for one sec, repeatedly.
#  But the interval increases each time by 1 more sec.

import time
import board
import digitalio


blinkTime = 1

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(blinkTime)
    led.value = False
    time.sleep(1)
    blinkTime += 1
