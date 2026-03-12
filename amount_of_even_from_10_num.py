even_num = 0
for i in range(10):
    num = float(input("Enter the number: "))
    if num % 2 == 0:
        even_num += 1
print("The amount of even numbers are:   ", even_num)