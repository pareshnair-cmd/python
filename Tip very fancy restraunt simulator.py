tip_percent = float(input("enter tip here:"))
def tip (tip_percent,amount = 550):
    return (amount + tip_percent)
total_bill = tip(tip_percent)
print (total_bill)