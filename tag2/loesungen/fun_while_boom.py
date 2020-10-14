def countdown(timer):
    start = timer
    ende = '???'
    while start > 0:
        print('Exploding in {} (nano)seconds{}'.format(start, ende))
        start -= 1
    print('Pufff!!!')


countdown(3)
countdown(5)
countdown(2)
countdown(9)
