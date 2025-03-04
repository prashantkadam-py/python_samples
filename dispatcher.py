'''
Reference 
python3.12

https://www.youtube.com/shorts/ykdzrsJ9fxQ

singledispatch is used to create a function that dispatches different implementations based on the type of the first argument.

'''


from functools import singledispatch, singledispatchmethod
from typing import Any, Union



@singledispatch
def display(arg: Any, verbose=False):
    raise NotImplementedError(f"Type {type(arg)} cannot be used with func......")



@display.register
def _(arg: Union[int,float], verbose=False) -> None:

    if verbose:
        print(f"Here is your Number : {arg}")
        return
    print(f"Number : {arg}")



@display.register
def _(arg: str, verbose=False):

    if verbose:
        print(f"Here is your text : {arg}")
        return
    print(f"Text : {arg}")




if __name__ == "__main__":
    display(10)
    display(14.3)
    display("hello")
    display(None)



