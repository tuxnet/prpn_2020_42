num = int(input("Please enter a number: "))
if num < 2:
    print(num, "is not prime")
else:
    i = 2
    while i * i <= num:
        if num % i == 0 and num != 2:
            print(num, "is not prime")
            break
        i += 1
    else:
        print(num, "is prime")
