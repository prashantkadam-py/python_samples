'''
Reference
https://www.youtube.com/watch?v=46_yfYC36JY&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=74
https://www.youtube.com/watch?v=D67-b2t-y4k&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=77

Encapsulation :
- Method Overriding (Runtime Polymorphism)
- Operator Overloading (Python allows operators to be overloaded by defining special methods)
- Duck Typing (Dynamic Polymorphism)
    the type of object is determined by its behavior rather than its class.
'''


class Animal:

    def __init__(self):
        pass

    def speak(self):
        return f"some sound"



class Dog(Animal):

    def speak(self):
        return f"bark!!!"


class Cat(Animal):

    def speak(self):
        return f"Meow!!!"





class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


if __name__ == "__main__":

    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak()) #duck typing example
    
    p1 = Point(2, 3)
    p2 = Point(4,5)
    p3 = p1 + p2
    print(f"Operator overloading example {p3.x, p3.y}")



       
