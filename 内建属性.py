class Person(object):
    def __init__(self,name):
        self.name = name
        self.address = "重庆"

    # 属性访问时拦截
    # 里面不能再用self.xxx 会造成死循环 又走__getattribute__这个方法
    def __getattribute__(self, item):
        print("---拦截了---")
        if item == "name":
            print("log name")
            return "redirect name"
        else:
            # 正常返回值
            temp = object.__getattribute__(self,item)
            print("temp:%s"%temp)
            return temp

    @staticmethod
    def run():
        print("---run---")


aa = Person("Playboy")
print(aa.name)
print(aa.address)

# 调用方法时也会走__getattribute__方法
# 1.先获取run属性对应的结果，应该是个方法
# 2.方法再调用
aa.run()

