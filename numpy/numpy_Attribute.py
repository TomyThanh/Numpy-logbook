import numpy as np


array1d = np.array([1,2,3])
array2d = np.array([[1,2,3], [4,5,6]])

print(array1d.ndim) #.ndim gibt die Dimension an
print("-------")
print(array2d.shape) #.shape gibt die Form an in einem Tuple z. B 2 * 3 (2 Vektoren mit jeweils 3 Elementen)
print(array1d.size) #.size gibt die Anzahl der Elemente
print(array2d.dtype) #.dtype gibt den Datentypen von den Elementen an
print(array1d.itemsize) #.itemsize gibt die Größe in Byte von jeweils einem Elementen
print(array2d.nbytes) #.nbytes gibt die Größe des Arrays an
print(array2d.T) #.T Spalte und Zeile werden getauscht

for element in array2d.flat: #Packt alle Elemente aus einem Array aus
    print(element)


# Copy und View

x = np.arange(9)
y = x.reshape(3,3) # View von x 
z = y[[0, 1]] # Gebe die erste und zweite Zeile von y an
u = np.copy(x) # Kopie von x und keine View von x


print(u.base)