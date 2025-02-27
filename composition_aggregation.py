'''
Reference 

ProgrammingKnowledge
https://www.youtube.com/watch?v=mPFc3JHLnz8

Composition and Aggregation
- Composition : 
    - interdependent
    - Once you delete main class it delets the other class
    - It represents part-of relationship

- Aggregation : 
    - independent
    - One object delete does not affect the other object
    - It represents Has a relationship
    

'''


class Salary(object):

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus


    def annual_salary(self):
        return (self.pay * 12) + self.bonus




class Employee(object):

    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)


    def total_salary(self):
        return self.obj_salary.annual_salary()



class Employee1(object):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary_obj = salary


    def total_salary(self):
        return self.salary_obj.annual_salary()

if __name__  == "__main__":
    #Composition Example
    emp = Employee("A", 32, 100000, 20000)
    print(emp.total_salary())

    #Aggregation Example
    salary = Salary(100000, 20000)
    emp = Employee1("A", 32, salary)
    print(emp.total_salary())

