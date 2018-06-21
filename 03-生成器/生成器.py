# a = (x*2 for x in range(10))
#
# for x in a:
#     print(x)


def test():
    i = 0
    while i < 5:
        yield i
        i += 1

a = test()
a.__next__()


