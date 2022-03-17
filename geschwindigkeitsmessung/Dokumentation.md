# Projekt Geschwindigkeitsmessung

## Anfangsüberlegungen

Es soll die Geschwindigkeit eines aufziehbaren Modellautos bestimmt werden.

Grundsätzlich gibt es zwei Messmethoden. Bei beiden wird die Geschwindigkeit über die Differenz der Zeit gemessen:

v = Δl / Δt

Dabei ist entweder Δl konstant, wenn man an zwei (oder mehr) bekannten Punkten jeweils eine Messung durchführt und die Geschwindigkeit über den Zeitunterschied zwischen diesen Messungen durchführt, wie z.B. bei Verwendung einer Lichtschrank oder Induktionsschleife.

Oder Δt ist konstant, z.B. bei der Messung mit einer Radarpistole. Hier wird an zwei (oder mehr) Zeitpunkten eine Messung durchgeführt, die jeweils die Entfernung zum Messgerät zurück liefert. Hieraus wird dann der Ortsunterschied berechnet und dann die Geschwindigkeit bestimmt.

In unserem Rahmen halten wir die Messung per Lichtschranke für praktikabel.
Dafür müssen wir zwei Lichtschranken in bekannter Entfernung zueinander aufbauen. Wir benötigen ein Programm, dass die Zeit zwischen Unterbrechung der ersten und der zweiten Lichtschranke misst und daraus im Anschluss die Geschwindigkeit berechnet und ausgibt.
