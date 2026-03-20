numbers = []
while True:
    user_input = input("Enter a number(or letter to stop): ")
    try:
        numbers.append(int(user_input))
    except ValueError:
        break
if numbers:
    print(f"The lowest number is: {min(numbers)}")