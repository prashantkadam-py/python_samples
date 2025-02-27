'''
Reference 

CampusX
https://www.youtube.com/watch?v=O-NrQvtorp0

Abstraction
- Abstract Class
- Abstract Method
'''


from abc import ABC, abstractmethod



class BankApp(ABC):

    def database(self):
        print("connected to database.......")


    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):


    def mobile_login(self):
        print("login into mobile.......")


    '''
    Parent class is enforcing to define this method by adding abstractmethod as an decorator in parent class
    TypeError: Can't instantiate abstract class MobileApp with abstract method security
    '''
    def security(self):
        print("mobile security...")



if __name__ == "__main__":
    obj = MobileApp()
    obj.mobile_login()
    obj.security()
