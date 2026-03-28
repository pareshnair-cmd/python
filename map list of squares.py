list1 = [2,4,8,7,3,1,5,6,10,9]
list2 = [22,48,87,21,36,11,50,63,110,99]
def add(a,b):
    return a + b
list3 = list(map(add,list1,list2))
print (list3)
def square(n):
    return n*n
print (list(map(square,list3)))
    