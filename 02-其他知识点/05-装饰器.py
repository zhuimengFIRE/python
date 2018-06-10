
def w1(func):
    print("---w1---")
    def func_in():
        print("---w1--func_in---")
        func()
    return func_in

def w2(func):
    print("---w2---")
    def func_in():
        print("---w2--func_in--")
        func()
    return func_in

# 多个装饰器 先走w2，w1下面是函数后才装饰w1
@w1 # 相当于f1 = w1(f1) 装饰器的原理
@w2
def f1():
    print("---f1---")

f1()
