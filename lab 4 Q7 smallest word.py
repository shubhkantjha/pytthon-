s = input("Enter a string: ")  # Input string
words = s.split()  # Split the string into words
smallest_word = min(words, key=len)  # Find the smallest word

print("The smallest word is:", smallest_word)
