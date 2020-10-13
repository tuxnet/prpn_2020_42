start = 10  # Startwert der Schleife, Countdown beginnt bei 10
while start > 0:  # solange der Startwert groeßer als 0:
    print('Exploding in {} seconds'.format(start))
    start -= 1  # ... wird der Startwert um 1 verringert. 
print('BOOM!!!')
