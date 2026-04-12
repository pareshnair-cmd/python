class IOstring:
    def __init__(self,str1):
        self.str1 = str1
    def uppercase(self):
        print(self.str1.upper())
    def __del__(self):
        print ("ob is destroyeddd")
ob = str(input("type somthing"))
ob234 = IOstring(ob)
print (ob234.uppercase())
del ob234
       