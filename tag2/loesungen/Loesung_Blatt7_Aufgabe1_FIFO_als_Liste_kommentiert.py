fifo = [] # die Variable 'fifo' verweist anfangs auf eine leere Liste
while True: # Endlosschleife
    k = input("> ") # der Nutzer wird mit input() zu einer Eingabe aufgefodert
    if k == "": # wenn keine Eingabe getaetigt wurde, als nur Enter gedrueckt
        break # wurde, dann wird die Schleife mit 'break' beeendet. 
    if k != "?": # wenn die gegenwaertige Eingabe kein ?
        fifo.append(k) # dann fuege der Liste diese mit append() hinzu
        print(fifo) # und gib die gesamte Liste auf dem Bildschirm aus.
    elif len(fifo) > 0: # ansonsten, also wenn es sich bei der gegenwaertigen
                        # Eingabe um ein '?' handelt und die Laenge der Liste
                        # groeßer als 0, dann
        print(fifo.pop(0)) # entferne das erste Element und gib diese aus
        print(fifo) # Auch unter dieser Bedingung wird die gesamte Liste
                    # auf dem Bildschirm ausgegeben. 
    else: # ansonsten
        print("List is empty") # handelt es sich um eine leere Liste
