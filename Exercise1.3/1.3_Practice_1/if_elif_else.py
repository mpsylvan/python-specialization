a = int(input("Enter a number "))
b = int(input("Enter a second number "))
operation = input("Enter '+'  for addition or '-' for subtraction. ")

if operation == "+" :
    result = str (a + b)
    print(f'Sum of {a, b} : {result}')
elif operation == "-" :
    result = str (a - b)
    print(f'Difference of {a, b} {result}')
else:
    print("Unknown operator. It must be + / - \n   ending program")
