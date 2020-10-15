def mysum(n, m=1):
    if n == m:
        return m
    else:
        return n + mysum(n - 1, m)


print(mysum(5, 2))
print(__name__)


if __name__ == '__main__':
    print(mysum(3))
    print(mysum(3, 2))
