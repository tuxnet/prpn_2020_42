# Eingabe einer Zahl mit Hilfe der eingebauten input()-Funktion. Die Eingabe 
# wird mit int() in eine ganze Zahl umgewandelt. 
num = int(input("Please enter a number: "))
if num < 2: # wenn die eingegebene Zahl kleiner als 2 ist, dann
    print(num, "is not prime") # handelt es sich um keine Primzahl
else: # ansonsten 
    for i in range(2, num): # die Zaehlvariable i wird von 2 bis 'num'
        # hochgezaehlt und 
        if num % i == 0 and num != 2:
            # wenn sich 'num' ganzzahlig durch die gegenwaertige Zahl i teilen
            # laesst und nicht gleich 2 ist:
            print(num, "is not prime") # dann handelt es sich um eine Primzahl
            break # und die Schleife wird mit 'break' beendet. 
    else: # andernfalls
        print(num, "is prime") # handelt es sich um eine Primzahl.
