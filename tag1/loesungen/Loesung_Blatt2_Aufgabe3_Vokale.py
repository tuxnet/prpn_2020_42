s = "Teststring"

count = 0
if ("a" in s) or ("A" in s):
    count += 1
if ("e" in s) or ("E" in s):
    count += 1
if ("i" in s) or ("I" in s):
    count += 1
if ("o" in s) or ("O" in s):
    count += 1
if ("u" in s) or ("U" in s):
    count += 1

if count == 0:
    print("Der Text enthält keine Vokale.")
elif count == 1:
    print("Der Text enthält nur eine Art von Vokal.")
else:
    print("Der Text enthält", count, "unterschiedliche Vokale.")
