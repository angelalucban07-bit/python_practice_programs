num = float(input("Enter the first number: "))
for i in range (9):
    next_num = float(input("Enter the next number: "))
    num -= next_num
print("The result number is:", num)