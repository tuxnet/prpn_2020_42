s = "Teststring"  # eine beliebige Zeichenfolge zum Testen

count = 0  # Variable zum Zaehlen der Vokale
if ("a" in s) or ("A" in s):  # wenn ein kleines oder großes "a" in s ...
    count += 1  # ... wird die Zaehlvariable um 1 erhoeht.
# Dies wird nach demselben Schema, beim Auftreten der uebrigen Vokale 
# (e, i, o, und u) durchgefuehrt:
if ("e" in s) or ("E" in s): 
    count += 1
if ("i" in s) or ("I" in s):
    count += 1
if ("o" in s) or ("O" in s):
    count += 1
if ("u" in s) or ("U" in s):
    count += 1

if count == 0:  # wenn kein Vokal in der Zeichenfolge s vorhanden:
    print("Der Text enthält keine Vokale.")
elif count == 1:  # wenn genau ein Vokal in der Zeichenfolge s vorhanden ist:
    print("Der Text enthält nur eine Art von Vokal.")
else:  # wenn mehr als ein Vokal in der Zeichenfolge s vorhanden sind:
    print("Der Text enthält", count, "unterschiedliche Vokale.")
