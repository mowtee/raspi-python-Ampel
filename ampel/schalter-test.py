import RPi.GPIO as gpio         # importiere Bibliotheken
import time

gpio.setmode(gpio.BOARD)        # definiere GPIO Overlay

gpio.setup(24,gpio.IN)          # Schalter

GPIO.wait_for_edge(24, GPRIO.FALLING)
print("Hallo")
