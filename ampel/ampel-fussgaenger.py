import RPi.GPIO as gpio         # importiere Bibliotheken
import time

gpio.setmode(gpio.BOARD)        # definiere GPIO Overlay

gpio.setup(29,gpio.OUT)         # Auto rot
gpio.setup(31,gpio.OUT)         # Auto gelb
gpio.setup(33,gpio.OUT)         # Auto gruen

gpio.setup(35,gpio.OUT)         # Fussgaenger rot
gpio.setup(37,gpio.OUT)         # Fussgaenger gruen

gpio.setup(24,gpio.IN)          # Ampelschalter
# gpio.setup(22,gpio.IN)          # Abbruchschalter


gpio.output(33,gpio.HIGH)       # Auto gruen
gpio.output(35,gpio.HIGH)       # FG rot
time.sleep(3)

# GPIO.add_event_detect(22, GPRIO.RISING)

try:
    while True:


        gpio.output(33,gpio.LOW)
        gpio.output(31,gpio.HIGH)
        time.sleep(2)
        gpio.output(31,gpio.LOW)
        gpio.output(29,gpio.HIGH)
        time.sleep(1)
        gpio.output(35,gpio.LOW)
        gpio.output(37,gpio.HIGH)
        time.sleep(5)
        gpio.output(35,gpio.HIGH)
        gpio.output(37,gpio.LOW)
        time.sleep(1)
        gpio.output(31,gpio.HIGH)
        time.sleep(1)
        gpio.output(29,gpio.LOW)
        gpio.output(31,gpio.LOW)

        gpio.output(33,gpio.HIGH)
        gpio.wait_for_edge(24, gpio.FALLING)


#        if GPIO.event_detected(22):
#            break


    gpio.cleanup()
    exit()

except KeyboardInterrupt:
    gpio.cleanup()
    exit()
