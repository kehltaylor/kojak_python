from math import *

# 1.

time = 6.892
distance = 19.7

# 2.

name = input("Input name")
age = input("Input age")
print(name, age)
name = str(input("Input name"))
age = int(input("Input age"))

# 3.

num = float(input("Input a float number"))
if num >= 0:
    print(sqrt(num))
else:
    print("Exception!")

# 4.

array = [str(input("Input a word")), str(input("Input a second word"))]
array.sort()
print(array[0])

# 5.

pSeuil = 2.3
vSeuil = 7.41
p = float(input("Input pression value"))
v = float(input("Input volume value"))
if p > pSeuil and v > vSeuil:
    print("!STOP!")
elif p > pSeuil and v <= vSeuil:
    print("Turn up the volume")
elif p <= pSeuil and v > vSeuil:
    print("Turn down the volume")
else:
    print("Ok")
