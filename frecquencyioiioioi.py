testdic = {'a':3,'b':2,'c':2,'d':2,'e':1}
print (testdic)
userfrec = int(input("which frecquency: "))
k = userfrec
res = 0
for key in testdic:
    if testdic[key] == k:
        res = res + 1
        print ("The frequency of your choice is : "+str(res))