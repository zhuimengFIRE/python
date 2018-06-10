
def w1(func):
    print("---w1---")
    def func_in():
        print("---w1--func_in---")
        return func() #这里func指向f1的内容，所以需要返回
    return func_in

@w1
def f1():
    print("---f1---")
    return "playboy"


re = f1()
print("return value:%s"%re)

