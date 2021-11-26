# Top Sigrid ADXL345 Library
# Timo Ostlender, Franz Roessler, Timo Sirinyan
# Dies ist eine Raspberry Pi Python Library fuer den Accelerometer ADXL345
# Siehe Dokumentation

import smbus
import RPI.GPIO as GPIO

# Korrekten I2C Bus für Raspberry Pi Version auswählen und SMBus initialisieren
revision = GPIO.RPI_REVISION
if revision >= 2:
    busNumber = 1
else:
    busNumber = 0
bus = smbus.SMBus(busNumber)

# ADXL345 Konstanten:
ADDRESS         = 0x53
BW_RATE         = 0x2C
POWER_CTL       = 0x2D

BW_RATE_1600HZ  = 0x0F
BW_RATE_800HZ   = 0x0E
BW_RATE_400HZ   = 0x0D
BW_RATE_200HZ   = 0x0C
BW_RATE_100HZ   = 0x0B
BW_RATE_50HZ    = 0x0A
BW_RATE_25HZ    = 0x09

RANGE_2G        = 0x00
RANGE_4G        = 0x01
RANGE_8G        = 0x02
RANGE_16G       = 0x03

MEASURE         = 0x08
AXES_DATA       = 0x32


class SigridADXL345:

    address     = none
    rate        = none
    range       = none

    def __init__(self, address = ADDRESS, rate, range):
        try:
            print("Initializing...")
            self.address = address
            self.setRate(rate)
            self.setRange(range)
            self.startMeasurement()
            print("Done!")
        except:
            print("Error!")
            exit()

    def setRate(self, rate):
        # Python dictionary mit moeglichen Werten für die Bandwidth und Output Data Rate
        # zum Mapping der Uebergabevariable verwenden:
        adxl345Rates = {
        1600:   BW_RATE_1600HZ,
        800:    BW_RATE_800HZ,
        400:    BW_RATE_400HZ,
        200:    BW_RATE_200HZ,
        100:    BW_RATE_100HZ,
        50:     BW_RATE_50HZ,
        25:     BW_RATE_25HZ
        }

        defaultRate = BW_RATE_100HZ
        if rate not in adxl345Rates:
            print ("Invalid Value for BW Rate! Set to default 100 Hz.")
        rate        = adxl345_rates.get(rate, defaultRate)

    def setRange(self, range):
        # Python dictionary mit moeglichen Werten für die g Range
        # zum Mapping der Uebergabevariable verwenden:
        adxl345Ranges = {
        16:     RANGE_16G,
        8:      RANGE_8G,
        4:      RANGE_4G,
        2:      RANGE_2G
        }

        defaultRange    = RANGE_2G
        if rate not in adxl345Rates:
            print ("Invalid Value for g-Range! Set to default 2g.")
        range           = adxl345Ranges.get(range, defaultRange)

    def startMeasurement(self):

    def getData(self, unit):


if __name__ == "__main__":
