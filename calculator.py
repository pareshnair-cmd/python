def add (x,y):
    print (x + y)
def sub (x,y):
    print (x - y)
def multi (x,y):
    print (x * y)
def div (x,y):
    print (x / y)
option = int(input("choose a operator: "))
print ("1. addition")
print ("2. subtraction")
print ("3. multiplication")
print ("4. division")
if option == 1:
    num,num2 = int(input("enter 2 numbers: "))
    print(add(num,num2))
if option == 2:
    num,num2 = eval(input("enter 2 numbers: "))
    print(sub(num,num2))
if option == 3:
    num,num2 = eval(input("enter 2 numbers: "))
    print(multi(num,num2))
if option == 4:
    num,num2 = int(input("enter 2 numbers: "))
    print(div(num,num2))   
