num = int(input("Please enter a number: "))
if num < 2:
    print(num, "is not prime")
else:
    for i in range(2, num):
        if num % i == 0 and num != 2:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
