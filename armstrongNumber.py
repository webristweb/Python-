num = int(input("enter a number here: "))

sum = 0
temp = num

while temp > 0:
    digit = temp%10
    cube = digit ** 3
    sum = sum + cube
    fd = temp // 10
    temp //=10

if sum == num:
    print("it is a armstrong number")
else:
     print("it is an not an armstron number")
       
