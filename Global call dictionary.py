Countrydict = {'india':'0091','austrailia':'0025','nepal':'00977','UK':'0044','USA':'0011'}
print ("Choose from these options:")
print ("1.india")
print ("2.austrailia")
print ("3.nepal")
print ("4.UK")
print ("5.USA")
call = str(input("Enter the country name"))
print (Countrydict.get(call))