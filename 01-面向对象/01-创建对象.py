class Car:
   
    def __init__(self):
        self.wheelNum = 4
        self.color = "白色"

    def move(self):
        print("车在移动")

    def toot(self):
        print("车在鸣笛")

car = Car()
print("车的颜色是:%s"%car.color)
print("车轮有%d个"%car.wheelNum)

