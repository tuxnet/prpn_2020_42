s = input("Enter a string: ")  # Benutzereingabe einer Zeichenfolge
# Die Variable s verweist im Folgenden auf eingegebene Zeichenfolge. 
print("Overall: ", len(s), "characters")  # Ermitteln der Zeichenfolgenlaenge
# mit Hilfe der eingebauten Funktion len() und Ausgabe mit print()
print("'Clean': ", len(s.rstrip()), "characters") # ohne Leerzeichen rechts
