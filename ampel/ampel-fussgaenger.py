# Python Script, um mittels Raspberry Pi eine Ampel darzustellen.
# Simuliert wird ein Fussgaengerueberweg mit einer Ampel fuer Autofahrer und einer fuer Fussgaenger.
# Dazu kommt der Knopf, den Fussgaenger benutzen, um gruen zu bekommen. Bei druecken des Knopfs schaltet die Autoampel
# erst auf rot, danach bekommen die Fussgaenger gruen. Langes halten des Knopfs beendet das Programm.

# Repository: https://github.com/mowtee/raspi-python-embedded
# Code, Anmerkungen, Schaltplan

import RPi.GPIO as gpio         # importiere Bibliotheken
import time

gpio.setmode(gpio.BOARD)        # definiere GPIO Overlay

# Definiere Ausgaenge fuer LED's und Eingang fuer Taster:

gpio.setup(29,gpio.OUT)         # Auto rot
gpio.setup(31,gpio.OUT)         # Auto gelb
gpio.setup(33,gpio.OUT)         # Auto gruen

gpio.setup(35,gpio.OUT)         # Fussgaenger rot
gpio.setup(37,gpio.OUT)         # Fussgaenger gruen

gpio.setup(24,gpio.IN)          # Ampelschalter
# gpio.setup(22,gpio.IN)          # Abbruchschalter

# Initialzustand herstellen:

gpio.output(33,gpio.HIGH)       # Auto gruen
gpio.output(35,gpio.HIGH)       # FG rot
time.sleep(3)


# GPIO.add_event_detect(22, GPRIO.RISING)

# Ampel auf Dauerschleife:

try:    # try/except Statement, um KeyboardInterrupt (Ctrl-C) abzufangen und vor dem Beenden gpio.cleanup() auszufuehren
    while True:


# Falls Knopf 3 Sekunden gehalten wird, Programm beenden:

        if gpio.input(24) == gpio.LOW:
            for t in range(6):
                if gpio.input(24) == gpio.LOW:
                    time.sleep(0.5)
                else:
                   break
                if t == 5:
                    gpio.cleanup()
                    exit()

# Autoampel auf rot schalten, Fussgaengerampel auf gruen schalten:

        gpio.output(33,gpio.LOW)
        gpio.output(31,gpio.HIGH)
        time.sleep(2)
        gpio.output(31,gpio.LOW)
        gpio.output(29,gpio.HIGH)
        time.sleep(1)
        gpio.output(35,gpio.LOW)
        gpio.output(37,gpio.HIGH)
        time.sleep(5)

# Autoampel auf gruen schalten, Fussgaengerampel auf rot schalten:

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


except KeyboardInterrupt:
    gpio.cleanup()
    exit()
