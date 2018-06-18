import types

class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

# 给类添加属性
aa = Person('playboy',26)
aa.address = '重庆'  # 这是给实例对象添加属性
print(aa.address)

bb = Person('jack',54)
# print(bb.address)  # 崩 因为bb没有address属性

Person.num = 100
cc = Person('jim',66)
print(cc.num)


# 给类添加方法
def run(self):
    print('---%srun---'%self.name)
    return run

dd = Person('jay',23)
dd.run = types.MethodType(run,dd)
dd.run()