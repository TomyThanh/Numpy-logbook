import numpy as np

np.random.seed(42)
salesData = np.random.randint(10, 100, (100, 3))
columns = ["Verkauften Einheiten", "Preis pro Einheit", "Gesamtkosten"]

gesamtumsatz = salesData[:, 0] * salesData[:, 1] - salesData[:, 2]
quadratUmsatz = np.power(gesamtumsatz, 2) # Alle Werte werden in Array hoch n genommen
wurzelUmsatz = np.sqrt(gesamtumsatz) # Die Wurzeln von allen Werten werden gezogen
logarithmusUmsatz = np.log(gesamtumsatz, 10) # Logarithmus von allen Werten wird gezogen
additionsUmsatz = np.add(gesamtumsatz, 100) # Alle Werte werden in Array mit n addiert (n kann auch ein Array sein, aber der Shape muss gleich sein)
subtraktionsUmsatz = np.subtract(gesamtumsatz, 100) # Alle Werte werden in Array mit n subtrahiert (n kann auch ein Array sein, aber der Shape muss gleich sein)
multiplikationsUmsatz = np.multiply(gesamtumsatz, 3) # Alle Werte werden in Array mit n mulitpliziert (n kann auch ein Array sein, aber der Shape muss gleich sein)
divisionsUmsatz = np.divide(gesamtumsatz, 2) # Alle Werte werden in Array mit n dividiert (n kann auch ein Array sein, aber der Shape muss gleich sein)
rundenUmsatz = np.round(gesamtumsatz) # Alle Werte werden aufgerundet oder abgerundet
höchsterUmsatz = np.argmax(gesamtumsatz) # Gibt den Index des höchsten Werts




print(additionsUmsatz)