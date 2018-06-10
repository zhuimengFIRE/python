
# 带有参数的装饰器可以用于区分 做不同的事

def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---func_in---")
            print("参数为:%s"%arg)
            if arg == "playboy":
                print("对了，这是playboy")
            else:
                print("不对")

            functionName()
        return func_in
    return func


# 1.先执行func_arg("playboy")函数，这个函数return的结果是func这个函数的引用
# 2.@func
# 3.使用@func对test进行装饰
@func_arg("playboy")
def test():
    print("---test---")

@func_arg("dasdas")
def other():
    print("---other---")


test()
other()

