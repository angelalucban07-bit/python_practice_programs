while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        if len(set(user_input)) < len(user_input):
            print("Duplicate")
        else:
            print("Unique")
    else:
        print("Invalid input")
        break
