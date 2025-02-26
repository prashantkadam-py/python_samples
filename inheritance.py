'''
Reference
CodeWithHarry

https://www.youtube.com/watch?v=-KsfUaQEY9Y&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=61
https://www.youtube.com/watch?v=4o7xSHgKlvI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=79
https://www.youtube.com/watch?v=Il7XMJJeXiA&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=80
https://www.youtube.com/watch?v=B4Q8zxRkm_I&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=81

Inheritance :
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hybrid Inheritance
- Hierarchical Inheritance
'''
##################################################################

#Single Inheritance

class Base:
    pass

class Derived(Base):
    pass


##################################################################
#Multiple Inheritance

class Base1:
    pass


class Base2:
    pass

class Derived(Base1, Base2):
    pass


print(f"Method Resolution Order of Multiple Inheritance : {Derived.mro()}")

##################################################################

#Multilevel Inheritance


class Base:
    pass

class Derived1(Base):
    pass


class Derived2(Derived1):
    pass


print(f"Method Resolution Order of Multilevel Inheritance : {Derived2.mro()}")

###################################################################################

#Hybrid Inheritance

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass


class Derived3(Derived1, Derived2):
    pass


print(f"Method Resolution Order of Hybrid Inheritance : {Derived3.mro()}")

################################################################################################

#Hierarchical Inheritance


class Base:
    pass


class Derived1(Base):
    pass

class Derived2(Base):
    pass

#############################################################################
