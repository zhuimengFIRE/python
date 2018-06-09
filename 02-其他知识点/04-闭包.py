# 闭包：函数里再定义函数，并且用到外面函数的参数，返回里面函数名

def test(number):
    print("-----1------")

    def test_in(count):
        print("-----2------")
        print(number+count)

    print("-----3------")
    return test_in

sum = test(100)
sum(1)
sum(30)
