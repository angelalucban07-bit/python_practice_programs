text = input("Enter a word and put space at the beginning: ")
while text.startswith(" "):
    text = text[1:]
print(f'{text}')