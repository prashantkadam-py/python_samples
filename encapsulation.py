"""
Reference
Krish Naik Hindi
https://www.youtube.com/watch?v=tyA4vD5BF3A&t=62s

Encapsulation
Access Modifiers 
- public
- protected
- private (Name Mangling)
 
"""



class Person:

    #constructor
    def __init__(self, name, age, dob):
        self.__name = name           #private access modifiers can be access within class
        self.__age = age             #private access modifiers 
        self._dob = dob              #protected access modifiers can be access by child class



    def display_info(self):
        return f"the person name is {self.__name} and the age is {self.__age} dob {self._dob}"



class Student(Person):


    def __init__(self, name, age, dob):
        super().__init__(name, age, dob)
        print(f"dob is {self._dob}")    


if __name__ == "__main__":

    p = Person("Prashant", 34, "19th Dec 1990")
    #print(p.__name)  #private varivable can't be accessed directly
    print(f"{dir(Person)}")
    print(f"Accessing private variable using name mangling : {p._Person__name}")
    print(f"{p.display_info()}")

    s = Student("Prashant", 34, "19th Dec 1990")
    print(f"{s.display_info()}")
