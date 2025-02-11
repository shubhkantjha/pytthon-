my_string = input("Enter a string: ")

first_char = my_string[0]
new_string = first_char + my_string[1:].replace(first_char, '$')

print("Modified string:", new_string)
