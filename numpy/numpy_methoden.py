import numpy as np

#Reshapen Methoden

sensor_daten = np.array([
    [10, 15, 20, 25], # Sensor 1
    [30, 35, 40, 45], # Sensor 2
    [50, 55, 60, 65], # Sensor 3
])

changedArray = sensor_daten.reshape(4, 3) #.reshape kann die Form des Arrays ändern (n*m) und -1 macht automatisch die beste Form
changedArray2 = sensor_daten.flatten() #.flatten macht ein Array flach
changedArray3 = sensor_daten.ravel() #.ravel macht ein Array flach UND verändert die Elemente wenn im Array etwas geändert wird
changedArray4 = sensor_daten.T #. T vertauscht die Zeilen und Spalten
changedArray5 = sensor_daten.transpose() # .transpose macht das gleiche
sensor_daten.sort() # Sortiert alle Werte
changedArray7 = np.insert(sensor_daten, 3, 12) # Fügt x Array an die 4te Stelle 
changedArray8 = np.append(sensor_daten, 23) # Fügt x an die letzte Stelle vom sensor_daten Array
changedArray9 = np.delete (sensor_daten, 1, axis = 1) # Löscht die zweite Spalte, da axis = 1 vertikal und axis = 0 horizontal
changedArray10 = np.concatenate(sensor_daten, sensor_daten, axis = 0) # Kombiniert zwei Arrays untereinander oder nebeneinander
changedArray13, changedArray12,changedArray11 = np.split(sensor_daten, 3) # Teilt sensor_daten in drei einzelne Arrays

for element in changedArray.flat: #Packt alle Elemente aus einem Array aus
    print(element)




# Andere Methoden

changedArray6 = np.any() #Überprüft ob alle true oder nicht sind
changedArray6[changedArray6 > 20 ] = 25 # Überprüft die Werte in Array und setzt sie dann auf m
durchschnittswertArray = sensor_daten.mean() #Berechnet den Durchschnitt der Werte im Array

print(changedArray10)