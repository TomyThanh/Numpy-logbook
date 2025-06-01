import numpy as np


np.random.seed(42) #.seed wie in Minecraft eine random Array aber vorgespeichert

temperaturen = np.random.randint(15, 35, (5,15))
cities = ["Berlin", "München", "Köln", "Hamburg", "Frankfurt"]
print(temperaturen)


resultat = temperaturen[:, :] # "Koordinaten" des Elements in einem Array AUFPASSEN [y, x]
#mit einem : kann man alle Werte von einer Zeile herausgeben
#wenn man einen Wert vor dem : angibt, dann bestimmt man wann der Startpunkt ist bzw. hinter = Endpunkt
#temperaturen[:3, :3] = 77  Ersetzen mit 77


resultat2 = temperaturen[:, ::3] #jeder n-ter Wert wird angegeben
resultat3 = temperaturen[:, 2::3] #jeder n-ter Werte wird angegeben und noch dazu fängt er bei m

resultat4 = temperaturen[0, :] > 30 #Zeigt an ob die Bedingungen für die Werte erfüllt ist oder nicht
resultat5 = temperaturen.mean(axis=1) #Gibt den Durchschnittswert an (Axis=1 Zeile und Axis = 0 Spalte)



print(resultat5) 