# Funktionsdefinitionen
def funOhneReturn():
    print("Zeile 1")
    print("Zeile 2")


def funMitReturn():
    print("Zeile 1")
    return "Zeile 2"


def funMitArgument(arg):
    print(arg * 2)


def funMitArgumenten(a, b, c):
    return a + b + c


# Funktionsaufrufe
# funOhneReturn()
# a = funOhneReturn()
# funMitReturn()
# b = funMitReturn()
# print(a)
# print(b)
funMitArgument(2)
funMitArgument('2')
c = funMitArgumenten(3, 5, 12)
print(c)
funMitArgumenten(2, 5, 'text')
