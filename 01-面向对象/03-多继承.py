
# 继承的子类不能访问父类的私有属性和私有方法
class base(object):
    def test(self):
        print("-----base test-----")

class A(base):
    def test(self):
        print("-----A test-----")

class B(base):
    def test(self):
        print("------B test------")

class C(A,B):
    pass


obj_c = C()
obj_c.test()
print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序
