#word1 = input("Please enter word 1: ")
#word2 = input("Please enter word 2: ")
word1 = 'tester'
word2 = 'Hello World'
common = ""
for letter in word1:
    if (letter in word2) and (letter not in common):
        common += letter
if common == "":
    print("The words do not share any characters.")
else:
    print("The words have the following characters in common:",
          common)
