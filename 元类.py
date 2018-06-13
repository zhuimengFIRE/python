
# 类也是对象
class Person(object):
    def out(self):
        print("---out---")
    pass

print(Person)

# 动态创建类
def choose_class(name):
    if name == "teacher":
        class Teacher(object):
            pass
        return Teacher
    else:
        class Student(object):
            pass
        return Student

myClass = choose_class("teacher")
print(myClass)
print(type(myClass))

# 使用type创建类 不带属性
test = type("Test",(),{})
print(test)

# 使用type创建带有属性的类
test = type("Test",(),{"name":"playboy"})
print(test.name)

# class Test:(object):
#     name = "playboy"


# 使用type创建带有方法的类
test = type("Person",(Person,),{"name":"playboy"})
print(test.name)
test.out(test)

# test = Person()
# test.out()

