print ("1. radius")
print ("2. diameter")
method = str(input("choose your calculation method for circumfrence: "))
if method == 'diameter':
    num = int(input("enter value of diameter: "))
    circle1 = 3.14 * num
    print (circle1)
if method == 'radius':
    num2 = int(input("enter value of radius: "))
    circle2 = 2 * 3.14 * num2
    print (circle2)