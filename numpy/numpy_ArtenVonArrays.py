import numpy as np

#normale Arrays

array1 = np.array([1,2,3,4,5])
array2 = np.arange(0, 10, 1) #[0; 10[
array3 = np.linspace(0,1,5) # teilt den Anfangs- und Endwert in gleichmäßige n-Teile 

#mehrdimensionale Arrays (Matrix)
array2d = np.array([[1,2,3], [4,5,6]])
array3d = np.array([[[1,2], [3,4], [5,6]]])

#mit reshape() in Matrix
specialArray = np.arange(12).reshape(3, 4) # 3*4 = 12


#SPEZIELLE ARRAYS

zeroArray = np.zeros((2,4)) #Array (Matrix) nur aus 0
onesArray = np.ones((3,4, 2)) #Array (Matrix) nur aus 1
sevenArray = np.full((3,3,), 7) #Array (Matrix) nur aus n
diag01Array = np.eye(4) #Array (Matrix) nur aus 0 aber eine diagonale aus 1 (quadratisch)
diagonalArray = np.diag([1,2,3,4])#Array (Matrix) nur aus 0 aber eine diagonale aus Ns (quadratisch)

#zufällige Arrays np.random.rand()

randomArray = np.random.rand(2, 4) #Zufälliges Array von 0-1 und shape (n, m = n * m)
randnArray = np.random.randn(3,3) #Zufälliges Array von 0-1 normalverteilt und shape (n, m = n * m)
randintArray = np.random.randint(0, 10, (3,3)) #Zufälliges Array von n-m € [n; m[ int-Werte und shape (x, y = x * y)
emptyArray = np.empty((2,2)) #Leeres Array mit shape (n, m = n * m)