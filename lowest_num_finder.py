numbers = []
while True:
    try:
        num =int(input("Enter a number (or a letter to stop): "))
        numbers.append(num)
    except ValueError:
        break
if numbers:
    print(f"The lowest number is: {min(numbers)}")