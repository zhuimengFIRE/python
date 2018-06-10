
def w1(func):
    print("---w1---")
    # *args和**kwargs处理不定长参数
    def func_in(*args,**kwargs): # 这里对应的带参数 因为f1此时指向这里
        print("---w1--func_in---")
        func(*args,**kwargs) # 这里必须带参数，因为此时func已经指向f1了
    return func_in

@w1
def f1(a):
    print("---f1---a=%d"%(a))

@w1
def f2(a,b,c):
    print("---f2-a=%d,b=%d,c=%d--"%(a,b,c))


f1(11)
f2(11,22,33)

