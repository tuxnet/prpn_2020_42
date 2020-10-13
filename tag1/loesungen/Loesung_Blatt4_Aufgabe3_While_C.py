total = 0
count = 0
new = None
while new != 0:
    new = int(input("Bitte eine Zahl eingeben: "))
    total += new
    if new != 0:
        count += 1
print ("Die Summe ist", total)
print ("Der Durchschnitt ist", total / count)
