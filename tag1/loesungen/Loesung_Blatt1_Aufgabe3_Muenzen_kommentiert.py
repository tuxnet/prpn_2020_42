# Anlegen von Konstanten fuer saemtliche Muenzen in Cents. 
CENTS_IN_2EURO = 200
CENTS_IN_EURO = 100
CENTS_IN_50CENT = 50
CENTS_IN_20CENT = 20
CENTS_IN_10CENT = 10
CENTS_IN_5CENT = 5
CENTS_IN_2CENT = 2
CENTS_IN_1CENT = 1

amount = 1156  # ein Testbetrag in Cents
cents = amount  # Verwendung einer Hilfsvariablen

ZweiEuro = cents // CENTS_IN_2EURO  # wieviel Zwei-Euro-Muenzen sind enthalten?
cents -= ZweiEuro * CENTS_IN_2EURO  # uebrig bleibende Cents nach Abzug der 2€s
Euro = cents // CENTS_IN_EURO  # Ein-Euro-Muenzen in den verbleibenden Cents?
cents -= Euro * CENTS_IN_EURO  # Cents nach Abzug der 1€-Muenzen
FunfzigCent = cents // CENTS_IN_50CENT  # usw.
cents -= FunfzigCent * CENTS_IN_50CENT
ZwanzigCent = cents // CENTS_IN_20CENT
cents -= ZwanzigCent * CENTS_IN_20CENT
ZehnCent = cents // CENTS_IN_10CENT
cents -= ZehnCent * CENTS_IN_10CENT
FunfCent = cents // CENTS_IN_5CENT
cents -= FunfCent * CENTS_IN_5CENT
ZweiCent = cents // CENTS_IN_2CENT
cents -= ZweiCent * CENTS_IN_2CENT
Cent = cents // CENTS_IN_1CENT
cents -= Cent * CENTS_IN_1CENT

# Ausgabe der einzelnen Muenzen mit Hilfe der print()-Funktion
print(amount, "Cent bestehen aus folgenden Muenzen:")
print("2€:", ZweiEuro)
print("1€:", Euro)
print("50Cent:", FunfzigCent)
print("20Cent:", ZwanzigCent)
print("10Cent:", ZehnCent)
print("5Cent:", FunfCent)
print("2Cent:", ZweiCent)
print("Cent:", Cent)
