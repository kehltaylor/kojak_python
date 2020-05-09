# 6

temp = str(input("Input a string"))
boolA = False
boolB = False
for i in range(len(temp)):
    if temp[i] == "@":
        boolA = True
if boolA and temp.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")


# 7.

for i in range(10):
    print("Message")


# 8.

for letter in "String":
    print(letter)


# 9.

a = 0
b = 10
for i in range(b - 1):
    a = a+1
    print("a = " + str(a))


# 10.

for i in range(10):
    print(b-i)


# 11.

temp = int(-1)
print(temp)
while temp > 10 or temp < 0:
    temp = int(input("Input a number"))


# 12.

for c in "character":
    print(c)

for item in ["cha", "rac", "ter"]:
    print(item)


# 13.

for i in range(14):
    if i != 0 and i % 3 == 0:
        print(i)

