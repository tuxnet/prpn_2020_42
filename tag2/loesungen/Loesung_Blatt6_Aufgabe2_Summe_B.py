def mysum(ende, start=1):
    summe = 0
    while start <= ende:
        summe += start
        start = start + 1
    return summe


print(mysum(5))
print(mysum(5, start=3))
print(mysum(5, 3))
