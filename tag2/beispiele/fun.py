def demo_fun(a, b, c=3, *name, **name2):
    print(a, b, c)
    print('***')
    print(type(name))
    for abc in name:
        print('arg:', abc)
    print('***')
    for xyz in name2:
        print('key:', xyz, 'value:', name2[xyz])


print('demo_fun is ready!')
