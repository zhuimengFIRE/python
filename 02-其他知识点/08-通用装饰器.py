
def w1(func):
    print("---w1---")
    def w1_in(*args,**kwargs):
        print("---w1_in---")
        return func(*args,**kwargs)
    return w1_in

@w1
def f1():
    print("---f1---")
    return "playboy"

@w1
def f2():
    print("---f2---")

@w1
def f3(a):
    print("---f3 a=%d---"%a)

re = f1()
print("return value:%s"%re)
re = f2()
print("f2 return value:%s"%re)
f3(11)


