# inheritance and polymorphism

from typing import Any


class animals:
    alive = True

    def eat(self):
        print("this animal is eating")
    
    def sleep(self):
        print("this animal is sleeping")


class rabbit(animals):

    def run(self):
        print("this rabbit is running")


class fish(animals):

    def swim(self):
        print("this fish is swimming")


class hawk(animals):

    def fly(self):
        print("this hawk is flying")



rabbit = rabbit()
fish = fish()
hawk = hawk()

print(rabbit.alive)
rabbit.eat()
rabbit.sleep()
rabbit.run()
print()
print(hawk.alive)
hawk.eat()
hawk.sleep()
hawk.fly()
print()
print(fish.alive)
fish.eat()
fish.sleep()
fish.swim()

# sources
# https://www.w3schools.com/python/python_inheritance.asp
# https://www.w3schools.com/python/python_polymorphism.asp
# F:\Youtube-dl\Coding\BroCode\Bro Code\Python tutorial for beginners 🐍\046 - 047 - 048 - 049 - 050 - 051 - 052

class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width


class Square(Rectangle):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        return self.lenght * self.width
    

class Cube(Rectangle):

    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def valume(self):
        return self.height * self.width * self.height
    

squre = Square(3, 3)
cube = Cube(3, 3, 3)

print()
print(squre.area())
print(cube.valume())
