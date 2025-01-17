
x = "global x"



'''
Order of variable scope execution is LEGB
L : local
E : Enclosed
G : Global
B : Builtins
'''
def outer_func():

    y = "nonlocal y"

    def inner_func():
        #nonlocal y  #to modify nonlocal y enable this line
        #global x    #to modify global x enable this line 
        print(x)
        y = "local y"
        print(y)

    inner_func()
    print(y)
    print(x)


outer_func()
print(x)



        

