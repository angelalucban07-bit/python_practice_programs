unique_numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num in unique_numbers:
        continue
    unique_numbers.append(num)
print("Unique numbers entered:", unique_numbers)