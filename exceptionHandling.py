x=int(input("Enter first Number:"))
y=int(input("Enter second Number:"))
try:
    z=x/y
    print(z)
except:
    print("Error")
else:
    Print("Koi error nhi aayi")
finally:
    print("bye")



'''cb=10000
while True:
    wb=int(input("Enter a amount:"))

    try:
        if(cb<wb):
            raise ValueError()
        cb=cb-wb
        print("Money Sent")
        print("Current Bal is",cb)

    except ValueError:
         print("Insuffient Balance")
         print("Current Bal is",cb)

    finally:
        print("bye")'''


