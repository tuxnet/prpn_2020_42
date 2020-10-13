start = 10
zeilenende = '!!!'
while start > 0:
    print('Exploding in {1} (nano)seconds{0}'.format(zeilenende, start))
    # print('Exploding in %s (nano)seconds%s' % (start, zeilenende))
    start -= 1
print('BOOM!!!')
