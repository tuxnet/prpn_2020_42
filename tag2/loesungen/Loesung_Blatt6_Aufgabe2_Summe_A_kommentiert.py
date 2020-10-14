def mysum(a): # Definition der Summenfunktion mit Eingabeargument 'a'
    summe = 0 # Hilfsvariable fuer die Gesamtsumme
    i = 1 # die Zaehlvariable wird auf 1 gesetzt
    while i <= a: # solange die Zaehlvariable 'i' kleiner als das Argument 'a'
        summe += i # wird die gegenwartige Zahl 'i' zur Gesamtsumme addiert. 
        i = i + 1 # die Zaehlvariable wird in jedem Schleifendurchlauf um 
                  # 1 erhoeht. 
    return summe # Nach Beendigung der Schleife wird die Gesamtsumme 
                 # zurueckgegeben. 

# Testen der Summenfunktion anhand von 3 Beispielaufrufen und unmittelbarer 
# Ausgabe mit der print()-Funktion.
print(mysum(2))
print(mysum(4))
print(mysum(5))
