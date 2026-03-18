numbers = []
for i in range(10):
    value = float(input(f"Enter a number: "))
    numbers.append(value)
    for n in numbers:
        if numbers.count(n) >= 1:
            print(n)