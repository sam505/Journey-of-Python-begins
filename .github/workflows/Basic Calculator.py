a = input("Enter the first number: ")
b = input("Enter the second number: ")
operator = input("Enter your preferred operation: ")

if operator == "Addittion" or operator =="addition" or operator =="ADDITION":
    print(int(a) + int(b))
elif operator == "Subtraction" or operator =="subtraction" or operator =="SUBTRACTION":
    print(int(a) - int(b))
elif operator == "Multiplication" or operator =="multiplication" or operator =="MULTIPLICATION":
    print(int(a) * int(b))
elif operator == "Division" or operator =="division" or operator =="DIVISION":
    print(int(a) / int(b))
else:
    print("Inavalid operator")
