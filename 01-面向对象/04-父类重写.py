class Person(object):
 
    def __init__(self):
        self.name = "playboy"
        self.age = "25"

    def run(self):
        print("父类----跑")

class Man(Person):
    def run(self):
        print("子类----跑")

my = Man()
my.run()
print(my.name)
print(my.age)

