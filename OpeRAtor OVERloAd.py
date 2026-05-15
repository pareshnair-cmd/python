class numbers:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a < other.a :
            return "ob1 lesser than ob2"
        else:
            return "ob1 is greater than ob2" 
    def __eq__(self,other):
        if self.a == other.a :
            return "ob1 is equal to ob2"
        else:
            return "ob1 is non equal to ob2"
ob1 = numbers(5275)
ob2 = numbers(5275) 
print (ob1 < ob2)
print (ob1 == ob2)