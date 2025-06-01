# Arrays speichern und laden
import numpy as np

beispielArray = np.array(range(9)).reshape(3,3)

np.savetxt("beispielArray.txt", beispielArray, delimiter=",") #Speichert Array als text-dokument
np.savetxt("beispielArray.csv", beispielArray, delimiter=",") #Speichert Array als csv-dokument
np.save("beispielArray.npy", beispielArray, delimiter=",") #Speichert Array als npy-dokument
beispielArray.tofile("beispielArray.dat") #Speichert Array als dat-dokument
# Delimiter ist ein Trennzeichen


beispielArray2 = np.loadtxt("beispielArray.txt", delimiter=",", dtype= int) #Lädt die Array-Datei und wandelt den dtype zu integer
beispielArray3 = np.fromfile("beispielArray.dat", dtype = int) #Lädt die dat-Datei als eindimensionalen Array
beispielArray4 = np.load("beispielArray.npy") #Lädt Array vom npy-Datei als normalen Shape

