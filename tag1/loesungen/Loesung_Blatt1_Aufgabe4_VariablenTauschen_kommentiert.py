# Variableninhalte tauschen
a = 17
b = 23
print("a =", a, " b =", b)
a += b  # Summe beider Variableninhalte
b = a - b  # Gesamtsumme minus b = Inhalt von a, auf welchen nun b verweist
a -= b  # Gesamtsumme minus b = Inhalt von b, auf welchen nun a verweist
print("a =", a, " b =", b)
