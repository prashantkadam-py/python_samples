"""
Reference 
Corey Schafer

https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
"""


print(f"\n\n {'#'*10} Strings {'#'*10}")
message = "Hello World"
print(f"Count sub-string appearances in string : {message.count('l')}")
print(f"Get position index of sub-string in string : {message.find('World')}") # if no substring found in main string it returns -1
print(f"Attributes and methods associated with variable : {dir(message)}")
print(f"Help function on class (str class) : {help(str)}")
print(f"Get information about specific method of class (str.lower): {help(str.lower)}")


print(f"\n\n {'#'*10} Numbers {'#'*10}")
a, b = 3, 2
print(f"Addition + :  {a+b}")
print(f"Subtraction - :  {a-b}")
print(f"Multiplication * :  {a*b}")
print(f"Division / :  {a/b}")
print(f"Floor Division // :  {a//b}")
print(f"Exponent ** :  {a**b}")
print(f"Modulus % :  {a%b}")
print(f"Absolute value of -3 :  {abs(-3)}")
print(f"Round upto 2 digits:  {round(100/3, 2)}")
