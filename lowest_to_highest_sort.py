#empty list
numbers = []
#loop
while True:
    try:
        num = int(input("Enter a number: "))
    #stops if invalid
    except ValueError:
        break
    numbers.append(num)
numbers.sort()
print("Sorted numbers from lowest to highest: ", numbers)