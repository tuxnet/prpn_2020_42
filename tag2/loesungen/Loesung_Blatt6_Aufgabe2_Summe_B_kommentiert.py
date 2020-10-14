def mysum(a,m=1): # Summendefinition mit zwei Eingabeargumenten:
                  # 'a' ist die Obergrenze und 'm' die Untergrenze
    summe = 0 # Hilfsvariable fuer die Gesamtsumme
    while m <= a: # solange 'm' kleiner oder gleich 'a' ist
        summe += m # wird der derzeitige Wert 'm' zur Gesamtsumme 'summe'
                   # addiert und
        m = m + 1 # 'm' um 1 erhoeht. 
    return summe

# Testen der Summenfunktion anhand von zwei Beispielen:
print(mysum(5))
print(mysum(5,m=3))
