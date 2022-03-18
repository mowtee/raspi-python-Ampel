import RPi.GPIO as GPIO         # importiere Bibliotheken
import time
from lcd import LCD             # LCD Bibliothek als Modul importieren und im globalen Namespace verfügbar machen

GPIO.setmode(GPIO.BCM)          # definiere GPIO Overlay // BCM, da LCD Bib BCM nutzt
GPIO.setup(20,GPIO.IN)          # definiere Pin 38 als Input // BCM Pin 20
GPIO.setup(21,GPIO.IN)          # definiere Pin 40 als Input // BCM Pin 21


ns_pro_s = 1000000000
distanz = 0.2                   # Distanz zwischen Lichtschranken in Metern
geschwindigkeit_ms = 0          
geschwindigkeit_kmh = 0
zeit1 = None
zeit2 = None
geschwindigkeit_schwelle_kmh = 5    # erlaubte Geschwindigkeit
anzeigedauer_sek = 3
messzeitpunkt = None


lcd = LCD()                     # LCD initialisieren



try:
    while True:
        if messzeitpunkt:
            if time.time() > (messzeitpunkt+anzeigedauer_sek):
                lcd.clear()
        if GPIO.input(20) == GPIO.HIGH and GPIO.input(21) == GPIO.LOW and zeit1 == None:
            zeit1 = time.time_ns()                      # time_ns() gibt die Zeit in ns seit der Unix Epoche zurück -> benötigt für Präzision
        if GPIO.input(21) == GPIO.HIGH and zeit1 and zeit2 == None:
            zeit2 = time.time_ns()
            zeit = zeit2 - zeit1
            geschwindigkeit_ms = distanz / (zeit / ns_pro_s)
            geschwindigkeit_kmh = geschwindigkeit_ms * 3.6
            geschwindigkeit_kmh_str = str(round(geschwindigkeit_kmh,2))
            zeit1 = None
            zeit2 = None
            messzeitpunkt = time.time()
            lcd.clear()
            if geschwindigkeit_kmh > geschwindigkeit_schwelle_kmh:
                lcd.message("Zu schnell! :(\n"+geschwindigkeit_kmh_str+" km/h")
            else:
                lcd.message("Danke! :)\n"+geschwindigkeit_kmh_str+" km/h")


except KeyboardInterrupt:                       # Benötigt, um GPIO zu releasen und sauber zu beenden
    GPIO.cleanup()
    exit()