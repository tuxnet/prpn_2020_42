fifo = []
while True:
    k = input("> ")
    if k == "":
        break
    if k != "?":
        fifo.append(k)
        print(fifo)
    elif len(fifo) > 0:
        print(fifo.pop(0))
        print(fifo)
    else:
        print("List is empty")
