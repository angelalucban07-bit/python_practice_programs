nums = []
while True:
    try:
        nums.append(float(input("Enter number: ")))
    except ValueError:
        break
print(max(nums))