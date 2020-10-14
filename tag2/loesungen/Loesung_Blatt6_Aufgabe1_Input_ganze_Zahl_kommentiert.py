def int_input(): # Definition der Funktion int_input() ohne Eingabeargumente
    inp = input('Please enter an integer: ') # Einlesen mit Hilfe von input()
    if inp.lstrip('-').rstrip().isdigit(): # bei der Eingabe wird auf der 
        # linken Seite der Zeichenfolge das '-' mit rstrip('-') entfernt. 
        # Daraufhin werden von der uebrig bleibenden Zeichenfolge die
        # Leerzeichen auf der rechten Seite entfernt. Bei der daraus
        # resultierenden Zeichenfolge wird ueberprueft ob es sich gaenzlich
        # um Zahlen handelt. Wenn dies der Fall ist, ...
        return int(inp.rstrip()) # ... wird der gegenwaertige Wert als 
                                 # Integer zurueckgegeben. 
    else: # ansonsten 
        print('This was not an integer.') # handelt es sich um keine Integer
        # return None # Passiert sonst implizit
        return int_input() # und die Funktion wird wieder rekursiv aufgerufen


# Test mit dreimaligem Aufruf:
a = int_input()
b = int_input()
c = int_input()
print(a, b, c) # und Ausgabe der der eingegebenen Zahlen 
# print(a + b if a and b else None, c)
