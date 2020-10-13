start = 0  # Variable 'start', die auf den Startwert 0 verweist.
ende = 5  # Variable 'ende', die auf den Endwert 5 verweist. 
total = 0  # Variable zum Speichern der Gesamtsumme. 
while start < ende:  # solange der Start- kleiner als der Endwert..
    new = int(input("Bitte eine Zahl eingeben: "))  # .. Eingabe einer neuen
    # Zahl durch den Benutzer. Da input() eine Zeichenfolge zurueckliefert, 
    # muss diese in eine ganze Zahl (einen Integer) umgewandelt werden. 
    total += new  # Die Variable 'total' wird um die gegenwaertige Zahl erhoeht
    start += 1  # Die Variable 'start' wird um 1 erhoeht. 
print ("Die Summe ist", total)  # Ausgabe der Gesamtsumme nach der Schleife
print ("Der Durchschnitt ist", total / start) # Ausgabe des Durchschnitts
