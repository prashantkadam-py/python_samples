'''
Descriptors

Reference 
https://www.youtube.com/watch?v=ovsvGtWD90Y

Live Python


'''

"""
Types of Descriptors 
1. Non Data Descriptors :
    Implements only __get__() method
    Example : property, classmethod, staticmethod

2. Data Descriptors :
    Implements __get__() and __set__() method
    Controls both retrieval and assignment


Use of Descriptors :
    1. property() uses internally
    2. staticmethod, classmethod
    3. ORMs (Django Models, SQLAlchemy) uses for database field validaton
    4. Enforcing integer type using descriptor
"""

class NonDataDescriptor():

    def __get__(self, instance, owner):
        print("Getting value.......")
        return 42



class DataDescriptor:

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        print("Getting value....") #can control get method
        return self.value 

    def __set__(self, instance, value):
        print("setting value....")
        self.value = value


class MyClass:
    attr = NonDataDescriptor()
    attr1 = DataDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    print(f"Non Data Descriptor access : {obj.attr}")
    print(f"Data Descriptor access : {obj.attr1}")
    obj.attr1 = 20
    print(f"After setting Data Descriptor value : {obj.attr1}")



