# Eingabe von zwei Worten mit Hilfe der input()-Funktion. 
word1 = input("Please enter word 1: ")  # Eingabe des ersten Wortes
word2 = input("Please enter word 2: ")  # Eingabe des zweiten Wortes
common = ""  # Auf die gemeinsamen Zeichen wird im folgenden mit 
# der Variablen 'common' verwiesen. 
for letter in word1:  # fuer jeden Buchstaben im ersten Wort, wird ...
    if (letter in word2) and (letter not in common):
        # ... wenn dieser Buchstabe auch im zweiten Wort, aber nicht
        # in den gemeinsamen Zeichen vorhanden ist, ...
        common += letter  # ... der Hilfszeichenfolge 'common' angehaengt. 
if common == "": # keine gemeinsamen Zeichen vorhanden sind:
    print("The words share no characters.")
else: # andernfalls:
    print("The words have the following in common:", common)
