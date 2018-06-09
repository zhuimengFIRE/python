class AA(object):
    def test(self):
        print("---AA--test----")

class BB(AA):
    def test(self):
        print("---BB--test----")

class CC(AA):
    def test(self):
        print("---CC--test----")

def Test(obj):
    print(obj.test())

bb = BB()
Test(bb)

cc = CC()
Test(cc)
