total = 0  # Variable zum Speichern der Gesamtsumme
count = 0  # Zaehlvariable
new = True  # Die Variable 'new' wird mit 'True'
# initialisiert, damit der folgende Vergleich wahr 
# zurueckliefert und somit die Schleife ausgefuehrt wird.
while new != 0:  # solange der Inhalt von 'new' nicht 0
    new = int(input("Bitte eine Zahl eingeben: "))  # Eingabe einer Zahl
    total += new  # Erhoehen des Inhaltes von 'total' um die eingegebene Zahl
    if new != 0:  # Wenn es sich bei der Eingabe um keine 0 handelte, ...
        count += 1  # ... wird die Zaehlvariable um 1 erhoeht. 
print ("Die Summe ist", total)  # Ausgabe der Gesamtsumme
print ("Der Durchschnitt ist", total / count)  # Ausgabe des Durchschnitts
