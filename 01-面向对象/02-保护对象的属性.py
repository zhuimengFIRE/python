# Python中用属性和方法的命名来区分私有和公有
# 前面有两个下划线则表示私有
class People(object):
    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self,newName):
        if len(newName) >= 5:
            self.__name = newName
        else :
            print("error,名字长度需要大于等于5")

person = People("aa")
person.setName("playboy")
print(person.getName())

person.setName("lili")
print(person.getName())

