# Write a simple calculator that adds, subtracts, multiplies, and divides two numbers.


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
C=input("Enter choice (1/2/3/4)")

if C in ['1', '2', '3', '4']:

    A = int(input("enter first number"))
    B = int(input("enter second number"))
    if (C == '1'):
        print(A + B)
    elif (C == '2'):
        print(A - B)
    elif (C == '3'):
        print(A * B)
    elif (C == '4'):
        print(A / B)
    else:
        print("operator can't declear")
else:
    print("Invalid input. Please choose (1/2/3/4)")
