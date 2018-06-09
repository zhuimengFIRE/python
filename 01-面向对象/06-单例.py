# __new__和__init__作用一样
# __new__必须有返回值，至少有一个参数cls
# 先执行__new__ 然后再执行__init__方法

class Singleton(object):
    __instance = None
    __first__init = False

    def __new__(cls,age,name):
        #如果__instance没有被赋值则创建一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self,age,name):
        if not self.__first__init:
            self.age = age
            self.name = name
            Singleton.__first__init = True

a = Singleton(10,"playboy")
b = Singleton(8,"boy")

print(id(a))
print(id(b))

print(a.age)
print(b.age)

a.age = 18 #给a指向的对象添加一个属性
print(b.age)

