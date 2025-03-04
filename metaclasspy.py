'''
MetaClass

Reference
https://www.youtube.com/watch?v=00acMGEfVlo

type(name, base, attributes) 

Decorator vs Metaclass

Decorator 
- Returns the same class after making changes (eg. monkey-patching)
- Lacks flexibility
- Isn't compatible to perform sub classing

Metaclass 
- Is used whenever a new class is created.
- Provides flexibility and customization of classes 
- Provides sub classing by using inheritance and converting object methods to static methods
for better optimization
'''


class Edureka:

    y = 12




class MetaOne(type):
    
    def __new__(cls, name, bases, attr): 
        return type(name, bases, attr)


class Python(metaclass=MetaOne):
    x = 10
    y = 20


if __name__ == "__main__":
    a = type('python', (Edureka, ), {'x' : 10})
    print(f"accessing class attribute : {a.x}")
    print(f"accessing base class attribute : {a.y}")

    a = Python()
    print(f"Accessing metaclass attributes : {a.x}")
    print(f"Accessing metaclass attributes : {a.y}")

