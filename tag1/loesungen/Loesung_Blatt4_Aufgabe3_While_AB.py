start = 0
end = 5
total = 0
while start < end:
    new = int(input("Bitte eine Zahl eingeben: "))
    total += new
    start += 1
print ("Die Summe ist", total)
print ("Der Durchschnitt ist", total / end)
