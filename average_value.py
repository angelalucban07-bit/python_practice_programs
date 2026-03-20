numbers = []
while True:
    try:
        numbers.append(float(input("Enter a number: ")))
    except ValueError:
        break
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print(average)