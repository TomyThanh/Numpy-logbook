# Numpy & Sensordaten-Analyse
import numpy as np

#1 Daten simulieren
zufälligePM = np.random.randint(5,151, (3, 365))

#2 Grundlegende Analyse

durchschnittSensor = np.mean(zufälligePM, axis = 1)
höchsteVerschmutzung = np.max(zufälligePM)

schlechteLuft = 0
for tage in zufälligePM.flat:
    if tage > 100:
        schlechteLuft = schlechteLuft + 1

#3 Vergleich zwischen Sensoren

sensorStandardabweichung = np.std(zufälligePM, axis = 1)
sensorhöchstedurchschnitt = np.argmax(durchschnittSensor) + 1 
print(f"Der {sensorhöchstedurchschnitt}. Sensor hat den höchsten Durchschnitt!")

#4 Bonus (für extra Herausforderung)
monats_tage = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
monatsnamen = ["Januar", "Februar", "März", "April", "Mai", "Juni",
               "Juli", "August", "September", "Oktober", "November", "Dezember"]

#1 Sensor
start_idx = 0
for i in range(12):
    end_idx = start_idx + monats_tage[i]
    durchschnittTempMonat = np.mean(zufälligePM[0,start_idx:end_idx])
    print(f"1.Sensor: {monatsnamen[i]}: {durchschnittTempMonat:.2f} PM2.5-WERT")
    start_idx = end_idx

#2 Sensor
start_idx = 0
for i in range(12):
    end_idx = start_idx + monats_tage[i]
    durchschnittTempMonat = np.mean(zufälligePM[1,start_idx:end_idx])
    print(f"2.Sensor: {monatsnamen[i]}: {durchschnittTempMonat:.2f} PM2.5-WERT")
    start_idx = end_idx

#3 Sensor
start_idx = 0
for i in range(12):
    end_idx = start_idx + monats_tage[i]
    durchschnittTempMonat = np.mean(zufälligePM[2,start_idx:end_idx])
    print(f"3.Sensor: {monatsnamen[i]}: {durchschnittTempMonat:.2f} PM2.5-WERT")
    start_idx = end_idx

#Tagesdurchschnitt aller Sensoren
tagesdurchschnittalleSensoren = np.mean(zufälligePM, axis = 0)


#Top 5 schlechteste Lufttage
zufälligePM.sort()
alleSensoren = zufälligePM.flatten()
schlechtesteLufttage = alleSensoren[1090:]
print(schlechtesteLufttage)