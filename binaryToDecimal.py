def convertBinary(n):
    if n > 1:
        convertBinary(n//2)
    print (n%2,end = "")
print("the binary of the given number is: ")

convertBinary(15)
