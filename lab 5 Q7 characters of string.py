my_string = input("Enter a string: ")

if len(my_string) < 2:
    result = ""
else:
    result = my_string[:2] + my_string[-2:]

print("Result:", result)
