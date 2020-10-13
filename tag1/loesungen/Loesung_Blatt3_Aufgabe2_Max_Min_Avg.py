zahl1 = float(input("Bitte geben Sie die 1. Zahl ein (1/3): "))
zahl2 = float(input("Bitte geben Sie die 2. Zahl ein (2/3): "))
zahl3 = float(input("Bitte geben Sie die 3. Zahl ein (3/3): "))

durchschnitt = (zahl1 + zahl2 + zahl3) / 3

maximum = max(zahl1, zahl2, zahl3)
minimum = min(zahl1, zahl2, zahl3)

print("Das Maximum beträgt:", round(maximum, 2))
print("Das Maximum beträgt: %.2f" % maximum)
print("Das Minimum beträgt:", round(minimum, 2))
print("Der Durchschnitt beträgt:", round(durchschnitt, 3))
