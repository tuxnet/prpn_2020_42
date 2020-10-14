def mysum(n, m=1):
    if n == m:
        return m
    else:
        return n + mysum(n - 1, m)


print(mysum(3))
print(mysum(5))
print(mysum(200, 199))
print(mysum(6, m=2))
print(mysum(5, m=3))
