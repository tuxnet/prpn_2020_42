# Eingabe von 3 Zahlen durch den Benutzer mit Hilfe der 
# eingebauten input()-Funktion. Da die input()-Funktion eine
# Zeichenfolge vom Typ String zurueckliefert, muss dieser
# Rueckgabewert zum Rechnen in eine Gleitkommazahl vom Typ
# Float umgewandelt werden. 
zahl1 = float(input("Bitte geben Sie die 1. Zahl ein (1/3): "))
zahl2 = float(input("Bitte geben Sie die 2. Zahl ein (2/3): "))
zahl3 = float(input("Bitte geben Sie die 3. Zahl ein (3/3): "))

durchschnitt = (zahl1 + zahl2 + zahl3) / 3  
# Durchschnitt = Summe / Gesamtlaenge

maximum = max(zahl1, zahl2, zahl3)  # Bestimmung des Maximums und 
minimum = min(zahl1, zahl2, zahl3)  # Minimums unter Verwendung der 
# eingebauten Funktionen max() und min(). 

# Ausgabe des Maximums, Minimums und des Durchschnitts
# nach Runden auf zwei Nachkommastellen. Der eingebauten Funktion
# round() kann die Anzahl der Nachkommastellen als zweites 
# Funktionsargument uebergeben werden. 
print("Das Maximum beträgt:", round(maximum, 2))
print("Das Maximum beträgt %.2f" %round(maximum, 2))
print("Das Minimum beträgt:", round(minimum, 2))
print("Der Durchschnitt beträgt:", round(durchschnitt, 2))
