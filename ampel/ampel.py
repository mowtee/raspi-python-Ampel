import RPi.GPIO as gpio         # importiere Bibliotheken
import time

gpio.setmode(gpio.BOARD)        # definiere GPIO Overlay

gpio.setup(29,gpio.OUT)         # rot
gpio.setup(31,gpio.OUT)         # gelb
gpio.setup(33,gpio.OUT)         # gruen

for i in range(3):              # Ampel 3 mal durchschalten
  gpio.output(29,gpio.HIGH)
  time.sleep(3)
  gpio.output(31,gpio.HIGH)
  time.sleep(1)
  gpio.output(29,gpio.LOW)
  gpio.output(31,gpio.LOW)
  gpio.output(33,gpio.HIGH)
  time.sleep(3)
  gpio.output(33,gpio.LOW)
  gpio.output(31,gpio.HIGH)
  time.sleep(1)
  gpio.output(31,gpio.LOW)

gpio.cleanup()
