a = 17
b = 23
print("a =", a, " b =", b)
a += b
b = a - b
a -= b
print("a =", a, " b =", b)
a, b = b, a
print("a =", a, " b =", b)
