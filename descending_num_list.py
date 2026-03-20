numbers = []
while True:
    try:
        num = int(input("Enter numbers (or letters to stop the program): "))
        numbers.append(num)
    except ValueError:
        break
print(sorted(numbers, reverse=True))