import RPi.GPIO as gpio         # importiere Bibliotheken
import time
from lcd import LCD             # LCD Bibliothek als Modul importieren und im globalen Namespace verfügbar machen

gpio.setmode(gpio.BOARD)        # definiere GPIO Overlay
gpio.setup(38,gpio.IN)          # definiere Pin 38 als Input
gpio.setup(40,gpio.IN)          # definiere Pin 40 als Input


ns_pro_s = 1000000000
distanz = 0.1                   # Distanz zwischen Lichtschranken in Metern
geschwindigkeit_ms = 0          
geschwindigkeit_kmh = 0
zeit1 = None
zeit2 = None
geschwindigkeit_schwelle_kmh = 5    # erlaubte Geschwindigkeit
anzeigedauer_sek = 3


lcd = LCD()                     # LCD initialisieren



try:
    while True:
        if time.time() > (messzeitpunkt+anzeigedauer_sek):
            lcd.clear()
        if gpio.input(38) == gpio.HIGH and gpio.input(40) == gpio.LOW and zeit1 == None:
            zeit1 = time.time_ns()                      # time_ns() gibt die Zeit in ns seit der Unix Epoche zurück -> benötigt für Präzision
        if gpio.input(40) == gpio.HIGH and zeit1 and zeit2 == None:
            zeit2 = time.time_ns()
            zeit = zeit2 - zeit1
            geschwindigkeit_ms = distanz / (zeit / ns_pro_s)
            geschwindigkeit_kmh = geschwindigkeit_ms * 3.6
            zeit1 = None
            zeit2 = None
            messzeitpunkt = time.time()
            #print(geschwindigkeit_ms)
            #print(geschwindigkeit_kmh)
            #print("Gemessene Geschwindigkeit betraegt " + str(round(geschwindigkeit_ms,2)) + " m/s oder " + str(round(geschwindigkeit_kmh,2)) + " km/h")
            lcd.clear()
            if geschwindigkeit_kmh > geschwindigkeit_schwelle_kmh:
                lcd.message("Zu schnell! :(\nSie fahren "+str(round(geschwindigkeit_kmh,2)+" km/h"))
            else:
                lcd.message("Danke! :)\nSie fahren "+str(round(geschwindigkeit_kmh,2)+" km/h"))


except KeyboardInterrupt:                       # Benötigt, um GPIO zu releasen und sauber zu beenden
    gpio.cleanup()
    exit()