print("~~~~~~~~~Mini calculator~~~~~~~~~~")

num1 = float(input("enter first number here: "))
num2 = float(input("enter second number here: "))

print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")
    
choice = int(input("enter your choice from 1-4: "))

if choice == 1:
    print("The addition of two number is",num1 + num2)
elif choice == 2:
    print("The subtraction of two number is",num1 - num2)
elif choice == 3:
    print("The multiplication of two number is",num1 * num2)
elif choice == 4:
    print("The division of two number is",num1 / num2)
else:
    print("invalid input")
    
