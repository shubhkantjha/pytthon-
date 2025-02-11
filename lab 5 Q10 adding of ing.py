my_string = input("Enter a string: ")

if len(my_string) >= 3:
    if my_string.endswith("ing"):
        my_string += "ly"
    else:
        my_string += "ing"
        
print("Modified string:", my_string)
