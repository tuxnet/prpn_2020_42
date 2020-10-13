# Eingabe einer Zahl mit Hilfe der eingebauten input()-Funktion. Die Eingabe 
# wird mit int() in eine ganze Zahl umgewandelt. 
num = int(input("Please enter a number: "))
if num < 2:  # wenn die Eingabe kleiner als 2 ist:
    # handelt es sich um keine Primzahl. 
    print(num, "is not prime")
else: # andernfalls:
    i = 2
    while i * i <= num:  # solange i*i kleiner als die eingegebene Zahl ist:
        # wenn sich die Zahl ganzzahlig durch die gegenwärtige Zahl i teilen
        # laesst und die Zahl nicht der 2 entspricht ...
        if num % i == 0 and num != 2: # dann
            print(num, "is not prime") # handelt es sich um keine Primzahl
            break # und die Schleife wird mit 'break' abgebrochen. 
        i += 1 # die Zaehlvariable wird um 1 erhoeht. 
    else: # ansonsten
        print(num, "is prime") # handelt es sich um eine Primzahl
