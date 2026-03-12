numbers = []
for i in range(10):
    val = float(input(f"Enter a number: "))
    numbers.append(val)
for n in numbers:
    if numbers.count(n) == 1:
        print (n)
