for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                links = "%d%d%d%d" % (a, b, c, d)
                rechts = "%d%d%d%d" % (d, c, b, a)
                links = 4 * int(links)
                rechts = int(rechts)
                if(a != b != c != d):
                    if(links == rechts):
                        print("A=%d, B=%d, C=%d, D=%d" % (a, b, c, d))
