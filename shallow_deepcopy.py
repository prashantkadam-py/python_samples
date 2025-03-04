'''
Shallow vs Deepcopy
'''


import copy


a = [[1,2,3], [4,5,6]]

b = copy.copy(a)

b[0][0] = 99

print(f"shallow copy, original : {a} new : {b} ")

c = copy.deepcopy(a)

c[0][0] = 100


print(f"deep copy, original : {a} new : {c} ")

