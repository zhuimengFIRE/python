class Money(object):
    def __init__(self):
        self.__money = 0 # 私有属性，外面不能直接访问

    def getMoney(self):
        return self.__money

    def setMoney(self,money):
        self.__money = money


# 使用property升级getter和setter方法
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self,money):
        self.__money = money

    money = property(getMoney,setMoney) # 外面就可以直接使用money属性了

# 使用property取代getter和setter方法
class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):  # 这里函数叫什么名字外面调用属性的时候就用什么名字
        return self.__money

    @money.setter 
    def money(self,money):
        self.__money = money








    






