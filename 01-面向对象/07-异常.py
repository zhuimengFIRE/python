# 打开一个不存在的文件会报IOError
try:
    print("-----1----")
    open("123.txt","r")
    print("-----2----")
except IOError:
    pass


try:
    print (num)
except NameError as result:
    # result存储异常信息
    print(result)

try:
    num = 100
    print(num)
except NameError as result:
    print(result)
else:
    print("没有捕捉到异常，真高兴")




