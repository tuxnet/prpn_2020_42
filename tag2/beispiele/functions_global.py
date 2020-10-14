def wertaendern():
    wert = 12
    print(wert)


def wertetest():
    global wert
    wert = 13
    print(wert)


def wertzeigen():
    print(wert)


wert = 42
print(wert)

wertaendern()
print(wert)
wertetest()
print(wert)
wertzeigen()
