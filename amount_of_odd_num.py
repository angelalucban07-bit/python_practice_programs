odd_num = 0
for i in range(10):
    num = float(input("Enter the number: "))
    if num % 2 == 1:
        odd_num += 1
print("The odd numbers is:", odd_num)