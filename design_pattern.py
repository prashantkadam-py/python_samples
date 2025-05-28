'''
Reference 
https://www.youtube.com/watch?v=-a1PFtooGo4&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=7
NeuralNine

Design Patterns:

    1. Factory Design Pattern
    2. Proxy Design Pattern
    3. Singleton Design Pattern
    4. Composite Design Pattern

'''


############################################################################

####### Factory Design Pattern ######################
from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """


class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"


    def person_method(self):
        print("I am a Student")



class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"


    def person_method(self):
        print("I am a Teacher")




class PersonFactory():
    
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        print("Invalid Type")
        return -1


choice = input("What type of person do you want to create ? \n")
person = PersonFactory.build_person(choice)
person.person_method()
##################################################################################

####### Proxy Design Pattern ##############################

from abc import ABCMeta, abstractstaticmethod


class Iperson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Interface Method """


class Person(IPerson):

    def person_method(self):
        print("I am a person!!!!")



class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()



    def person_method(self):
        print("I am the proxy functionality.")
        self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
###################################################################################

########### Singleton Design Pattern ##############################

from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ Implement in child class"""


class PersonSingleton(IPerson):

    __instance = None


    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance


    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once...........")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name : {PersonSingleton.__instance.name}")
        print(f"Age : {PersonSingleton.__instance.age}")

a = PersonSingleton("XYZ", 30)
a.get_instance()
a.print_data()

#b = PersonSingleton("AAA", 40) #not allowed to instantiate new object

###############################################################################

############# Composite Design Pattern ############

from abc import ABCMeta, abstractstaticmethod, abstractmethod


class IDepartment(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """


    @abstractstaticmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees


    def print_department(self):
        print(f"Accounting Department: {self.employees}")



class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees


    def print_department(self):
        print(f"Development Department: {self.employees}")



class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []



    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees


    def print_department(self):
        print(f"Parent Department Base Employees : {self.base_employees}")
        
        for dept in self.sub_depts:
            dept.print_department()

        print(f"Total employees : {self.employees}")


d1 = Accounting(100)
d2 = Development(200)

d3 = ParentDepartment(30)

d3.add(d1)
d3.add(d2)

d3.print_department()

#################################################################################

