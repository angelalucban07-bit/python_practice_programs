# 1. Get the original text and the prefix to look for
text = input("Enter the full text: ")
prefix = input("Enter the prefix to remove: ")

# 2. Check if the text actually starts with that prefix
# We compare the start of the 'text' to the 'prefix'
if text[:len(prefix)] == prefix:
    # 3. If it matches, we slice from the end of the prefix onwards
    result = text[len(prefix):]
else:
    # 4. If it doesn't match, we keep the original text
    result = text

print(f"Result: {result}")