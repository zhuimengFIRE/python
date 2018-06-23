# 创建生成器 列表的方式[]改成()
a = (x*2 for x in range(5))

# 访问
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a)) # 等价于print(a.__next__())

#for x in a:
#    print(x)


# 创建生成器的第二种方法 利用yield
# 如果函数里出现了yield，就不叫函数了，叫生成器
def fib(num):
    print("fib")
    n = 0
    a,b = 0,1
    while n<num:
        print("---1---")
        yield b
        print("---2---")
        a,b = b,a+b
        n += 1
    return 'done'

for x in fib(5):
    print(x)

fib(5) # 这时候返回一个生成器对象，不会执行fib里面的print("fib")语句


