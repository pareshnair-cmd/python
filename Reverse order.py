num = 56000
print(f"The number is: {num}")
while num > 0 and num < 10:
    print("number has 1 digit")
    break
while num > 10 and num < 100:
    print("number has 2 digits")
    break
while num > 100 and num < 1000:
    print("number has 3 digits")
    break
while num > 1000 and num < 10000:
    print("number has 4 digits")
    break
while num >= 10000:
    print("number has more than 4 digits")
    break