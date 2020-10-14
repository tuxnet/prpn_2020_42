def mysum(n, m=1): # Summendefinition mit zwei Eingabeargumenten: 
                   # 'n' Obergrenze und 'm' Untergrenze der Summe.
    if n == m: # Abbruchbedingung: Wenn Ober- gleich Untergrenze
        return m # dann gib 'm' zurueck. 
    else: # andernfalls (also wenn n groeßer als m)
        return n + mysum(n - 1, m) # addiere n zudem was der rekursive 
                                   # Funktionsaufruf mit 'n-1' als Obergrenze
                                   # zurueckgibt. 

# Testen der rekursiven Summenfunktion
print(mysum(3))
print(mysum(5))
print(mysum(200, 199))
print(mysum(6, m=2))
print(mysum(5, m=3))
