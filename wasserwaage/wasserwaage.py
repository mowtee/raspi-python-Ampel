# Top Sigrid ADXL345 Wasserwaage
# Timo Ostlender, Franz Roessler, Timo Sirinyan
# Dies ist eine Wasserwaagen-App für Raspberry Pi, ADX345 und Python.
# Zur Anzeige werden 5 LED's benutzt. Es kann zwischen Horizontal- und Vertikalmodus umgeschaltet werden.
# Siehe Dokumentation

import sigridAdxl345
import RPi.GPIO as gpio
import math as m
from time import sleep

gpio.setup(29,gpio.OUT)         # LED Center
gpio.setup(31,gpio.OUT)         # LED X+
gpio.setup(33,gpio.OUT)         # LED X-
gpio.setup(35,gpio.OUT)         # LED Y+
gpio.setup(37,gpio.OUT)         # LED Y-

gpio.setup(24,gpio.IN)          # Umschalter Horizontal- / Vertikalmodus

rate        = 100
range       = 2
unit        = g

horizontal  = True              # Boolean: Horizontal-Modus (True) / Vertikalmodus (False)

print("Top Sigrid Wasserwaage\n======================\n")
print()
try:
    threshold   = int(input("Genauigkeit in Grad: "))
except:
    print("Ungültig! Benutze Standard-Genauigkeit 3 Grad")
    threshold   = 3
print()


sigridADXL345 = SigridADXL345(rate, range)      # Neues Objekt der SigridADXL345 Klasse erzeugen (100 Hz, 2g)

try:
    while True:

        if gpio.input(24) == gpio.LOW:          # Falls Umschalter gedrueckt wird, horizontal invertieren
            horizontal = not horizontal

        if horizontal == True:                  # Mapping der Achsen fuer die spaetere Berechnung
            a = 0                               # data[0] = X-Wert, data[1] = Y-Wert, data[2] = Z-Wert des Sensors
            b = 1                               # Im Horizontal-Modus entsprechen die Berechnungs-Achsen den Sensor-Achsen, d.h. rotX = Rotation um X-Achse in Grad
            c = 2                               # Im Vertikalmodus kippen wir den Sensor um die Y-Achse. Dadurch wird der Sensor Z-Achse zur X-Achse in der Berechnung
            d = 1                               # Im Horizontalmodus zeigt die Sensor Z-Achse nach oben, im Vertikalmodus die Sensor X-Achse aber nach unten. d setzt entsprechend das Vorzeichen in der Berechnung
        elif horizontal == False:
            a = 2
            b = 1
            c = 0
            d = -1

        data        = sigridADXL345.getData(unit)

        rotX        = m.degrees(m.atan(data[b]/(d*data[c])))        # Prinzip der Berechnung siehe Dokumentation

        rotY        = m.degrees(m.atan(data[a]/(d*data[c])))

        gpio.output(29,gpio.LOW)                # Zuruecksetzen der LED's fuer einen sehr kurzen Augenblick
        gpio.output(31,gpio.LOW)
        gpio.output(33,gpio.LOW)
        gpio.output(35,gpio.LOW)
        gpio.output(37,gpio.LOW)

        if rotX > threshold:                    # Anzeigen der Ergebnisse mittels der LED's
            gpio.output(37,gpio.HIGH)

        if -rotX < -threshold:
            gpio.output(35,gpio.HIGH)

        if rotY > threshold:
            gpio.output(33,gpio.HIGH)

        if -rotY < -threshold:
            gpio.output(31,gpio.HIGH)

        if abs(rotX) < threshold or abs(rotY) < threshold:
             gpio.output(29,gpio.HIGH)

        time.sleep(0.1)                         # Wiederholrate 10 Hz


except KeyboardInterrupt:                       # Wenn Programm beendet mittels Ctrl-C GPIO's sauber aufraeumen
    print("Beendet")
    gpio.cleanup()
    exit()
