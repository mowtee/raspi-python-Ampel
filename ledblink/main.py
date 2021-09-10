import RPi.GPIO as gpio       # importiere Bibliotheken
import time
gpio.setmode(gpio.BOARD)      # definiere GPIO Overlay
gpio.setup(26,gpio.OUT)       # definiere Pin 26 als Output
for i in range(10):           # LED 10 mal an & aus
  gpio.output(26,gpio.HIGH)   # Pin 26 hoch auf 3,3V
  time.sleep(1)               # 1 Sekunde warten
  gpio.output(26,gpio.LOW)    # Pin 26 runter auf 0V
  time.sleep(1)
gpio.cleanup()
