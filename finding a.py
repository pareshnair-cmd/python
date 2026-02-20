word = str(input("enter string"))
for i in word:
    if i == 'a':
        print ("a is found")
        break
    else:
        print("a is not found")
print (i)