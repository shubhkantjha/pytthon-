string = input("Enter a string: ")
words = string.split()  # Split the string into words
result = []

for word in words:
    if len(word) == 1:
        result.append(word.upper())  # Capitalize single-letter words
    else:
        result.append(word[0].upper() + word[1:-1] + word[-1].upper())  # Capitalize first and last letter

print("Transformed string:", ' '.join(result))
