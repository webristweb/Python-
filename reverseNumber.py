
num = int(input("enter a number here: "))

reverse_num = 0
while num != 0:
    digit = num%10
    reverse_num = reverse_num*10 + digit
    num = num//10

print("the reverse of the given number is",reverse_num)
