def int_input():
    inp = input('Please enter an integer: ')
    if inp.lstrip('-').rstrip().isdigit():
        return int(inp.rstrip())
    else:
        print('This was not an integer.')
        return None # Passiert sonst implizit
        # return int_input() # Rekursiver Aufruf


a = int_input()
b = int_input()
c = int_input()
print(a, b, c)
