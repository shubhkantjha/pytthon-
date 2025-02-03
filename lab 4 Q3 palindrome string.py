s = input("Enter a string: ")  # Take input
s = s.lower()  # Convert to lowercase

if s == s[::-1]:  # Check if string is equal to its reverse
    print("Palindrome")
else:
    print("Not a palindrome")
