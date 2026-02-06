symbol = input("Enter a symbol: ")
print(f"You entered: {symbol}")
if not symbol.isalpha():
    print("This is not a letter.")
else:
    print("This is a letter.")