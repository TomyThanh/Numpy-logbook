# Statistik mit Arrays

import numpy as np

beispielArray = np.array(range(16)).reshape(4,4)
print(beispielArray)

beispielArray2 = np.array([1,2,3,4, -1 , -2 , -3, -4]).reshape(2,4)


ergebnis = np.mean(beispielArray, axis = 0) # Bestimmt den Mittelwert des Arrays axis = 0 Mittelwert der Spalten
ergebnis2 = np.sum(beispielArray, axis= 0) # Addiert alle Werte in eine Spalte oder Zeile oder ganzen Array
ergebnis3 = np.min(beispielArray) #Bestimmt den minimalen Wert der Axen oder des ganzen Arrays
ergebnis4 = np.max(beispielArray, axis = 0) #Bestimmt den maximalen Wert der Axen oder des ganzen Arrays
ergebnis5 = np.var(beispielArray) # Bestimmt die Varianz (Maß für die Abweichung vom Mittelwert)
ergebnis6 = np.std(beispielArray, axis = 1) # Bestimmt die Standard Abweichung
ergebnis7 = np.corrcoef(beispielArray2) # Bestimmt den Korrelationskoeffizient




print(ergebnis7)