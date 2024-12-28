class Employee:
    
    raise_amount = 1.1 #class variable
    no_of_employees = 0

    def __init__(self, first, last, pay):
        """
        self : instance of employee
        self.first : instance attributes
        """
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"
        Employee.no_of_employees += 1 # referring class variable

    def fullname(self):
        """
        fullname : instance method
        """
        return f"{self.first} {self.last}"

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #class variable can be accessed using self or by specifying class name self.raise_amount / Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    @classmethod
    def from_string(cls, emp_str):
        """
        Using a classmethod like constructor to create an Employee instance
        by parsing formatted string and avoiding rewriting / for-loop to construct these objects 
        """
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def isworkday(day):
        """
        static method it logically belongs to the class 
        but it does not uses any class or instance reference
        """
        if day.weekday() in (5, 6):
            return False
        return True



class Developer(Employee):
    raise_amount = 1.4

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay) #calling parent class init method 
        #Employee.__init__(self, first, last, pay) #another way to call parent class init method
        self.language = language


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        print(f"Employees : {self.employees}")

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}" )

        




if __name__ == "__main__":
    print(f"No of employees created : {Employee.no_of_employees}")
    emp_1 = Employee("prashant", "kadam", 50000) #creating an instance emp_1 of Employee class
    emp_2 = Employee("test", "user", 10000)
    print(f"No of employees created : {Employee.no_of_employees}")
    print("Employee instance method full name : ", emp_1.fullname()) #instance method emp_1 is passed as self 

    print("Employee instance method full name : ", Employee.fullname(emp_1)) #another way to call class method and passing instance to that method
    print("emp_1 pay : ", emp_1.pay)
    emp_1.apply_raise()
    print("emp_1 pay : ", emp_1.pay)
    emp_1.raise_amount = 1.5
    emp_1.apply_raise()
    print("Class Variable : ", Employee.raise_amount)
    print("emp_1 Instance Variable : ", emp_1.raise_amount)
    print("emp_2 Instance variable : ", emp_2.raise_amount)

    print(f"Employee class name space : {Employee.__dict__} ")
    print(f"Employee instance emp_1 name space : {emp_1.__dict__} ")
    
    Employee.set_raise_amount(1.6) #calling class method to set class variable
    emp_1.set_raise_amount(1.65)   #calling class method using instance it sets class variable 
    print(Employee.raise_amount)
    print(emp_2.raise_amount)
    print(emp_1.raise_amount)

    new_emp_1 = Employee.from_string("prashant-kadam-60000") # Using classmethod as constructor and eliminating split operation outside of class
    print(new_emp_1.email)
    print(new_emp_1.pay)
    import datetime
    my_date = datetime.datetime.now()
    print(f"Is workday : {Employee.isworkday(my_date)}")


    #print(help(Developer)) #Check Method resoltion order and other details

    dev_1 = Developer("Test 1", "user 1", 30000, "Python")
    dev_2 = Developer("Test 2", "user 2", 20000, "Java")

    mgr_1 = Manager("prashant", "kadam", 60000, employees=[dev_1])

    print(f"Manager Email : {mgr_1.email}")
    print(f"Manager pay : {mgr_1.pay}")
    mgr_1.print_employees()
    mgr_1.add_emp(dev_2)
    mgr_1.print_employees()
    
    print(f"mgr_1 isinstance of developer class : {isinstance(mgr_1, Developer)}")
    print(f"mgr_1 isinstance of employee class : {isinstance(mgr_1, Employee)}")
    print(f"Manager issubclass of Employee : {issubclass(Manager, Employee)}")
    print(f"Developer issubclass of Employee : {issubclass(Developer, Employee)}")
    print(f"Manager issubclass of Developer : {issubclass(Manager, Developer)}")

