# Projekt Geschwindigkeitsmessung

## Anfangsüberlegungen

Es soll die Geschwindigkeit eines aufziehbaren Modellautos bestimmt werden.

Grundsätzlich gibt es zwei Messmethoden. Bei beiden gilt die grundsätzliche Definition der Geschwindigkeit:

v = Δl / Δt

Geschwindigkeit ist also zurückgelegte Wegstrecke durch vergangene Zeit.

Zur Messnung hält man dabei entweder Δl konstant, indem man an zwei (oder mehr) bekannten Punkten mit bekannter Entfernung jeweils eine Messung durchführt und die Geschwindigkeit über den Zeitunterschied zwischen diesen Messungen durchführt, wie z.B. bei Verwendung zweier Lichtschranken oder Induktionsschleifen.

Oder Δt wird konstant gehalten, wie z.B. bei der Messung mit einer Radarpistole. Hier wird an zwei (oder mehr) bekannten Zeitpunkten eine Messung durchgeführt, die jeweils die Entfernung zum Messgerät zurück liefert. Hieraus wird dann der Ortsunterschied berechnet und dann die Geschwindigkeit bestimmt.

In unserem Rahmen halten wir die Messung per Lichtschranke für praktikabel.
Dafür müssen wir zwei Lichtschranken in bekannter Entfernung zueinander aufbauen. Wir benötigen ein Programm, dass die Zeit zwischen Unterbrechung der ersten und der zweiten Lichtschranke misst und daraus im Anschluss die Geschwindigkeit berechnet und ausgibt.

Zur Ausgabe haben wir eine Anzeige per LCD gewählt - ganz nach dem Vorbild der bekannten Geschwindigkeitsanzeigetafeln im Straßenverkehr.

Schauen wir uns die Logik des Programms an:

![](/users/timo/projects/raspi-python-embedded/geschwindigkeitsmessung/flowchart.png)

Ganz grundsätzlich speichert das Programm zwei Zeiten zeit1 und zeit2, berechnet die zeitliche Differenz zwischen den beiden und teilt im Anschluss die bekannte, im Quelltext hinterlegte Distanz durch diese Zeit um dadurch die Geschwindigkeit zu bestimmen.
Das Programm durchläuft dabei in hoher Frequenz fortlaufend seine Logik. Diese muss also entscheiden, welche Bereiche im Code in dem aktuellen Durchlauf angesteuert werden.

Betrachten wir zunächst den Bereich bei 2. Hier wird entschieden, ob eine neue Messung gestartet werden soll, oder nicht. Nach jeder erfolgten Messung werden die beiden Zeiten zeit1 und zeit2 auf None gesetzt, also gelöscht. Das Programm prüft nun, ob diese beiden Zeiten None sind. Ist dies nicht der Fall, läuft gerade eine Messung. Es darf also keine neue zeit1 gespeichert werden.
Sind aber beide Zeiten Null, so wird die Messung in dem Moment gestartet, in dem die erste Lichtschranke unterbrochen wird, indem die aktuelle Zeit in Nanosekunden in zeit1 gespeichert wird.
Da die Frequenz der Durchläufe hoch ist, ist die erste Lichtschranke beim nächsten Durchlauf immer noch unterbrochen. Es wird aber keine neue Messung gestartet, da zeit1 gesetzt ist.

Die Messung ist beendet, sobald die zweite Lichtschranke unterbrochen wird. Dies wird bei 3 geprüft. Wenn zeit1 gesetzt ist, zeit2 nicht gesetzt ist und die zweite Lichtschranke unterbrochen wird, wird in zeit2 die aktuelle Zeit gespeichert.
Das Programm fährt dann mit der Berechnung der Geschwindigkeit fort, löscht zeit1 und zeit2, leert die LCD Anzeige und entscheidet, ob die gemessene Geschwindigkeit größer als die erlaubte ist, oder nicht. Danach wird die Geschwindigkeit zusammen mit einer entsprechenden Anzeige (Danke! :) oder Zu schnell! :( ) auf dem LCD ausgegeben.

Alles was wir nun noch brauchen, ist die Leerung der LCD-Anzeige, wenn eine gewisse Zeit lang keine Messung durchgeführt wurde.
Dies haben wir 
