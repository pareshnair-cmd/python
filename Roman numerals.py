class numeral:
    def roman(self,num,ro):
        self.num = num
        self.ro = ro
inputnumber = (int(input('enter number')))
if inputnumber <=3:
    for i in range(inputnumber):
        print ('i') 
if inputnumber == 4:
    for i in range(1):
        print ('i')
        print ('v')
if inputnumber == 5:
    for i in range(1):
        print ('v')            
if inputnumber == 6 or inputnumber == 7 or inputnumber == 8:
    for i in range(1):
        print ('v')
    for j in range(inputnumber - 5):
        print ('i')
if inputnumber == 9:
    for i in range(1):
        print ('i')
        print ('x')
if inputnumber >= 10:
    for i in range(1):
        print ('x')
    for j in range(inputnumber - 10):
        print ('i')