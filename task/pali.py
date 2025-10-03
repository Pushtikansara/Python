import string

def is_palindrome(text):
    # Remove punctuation and spaces, and convert to lowercase
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

# Test the function
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("It's a palindrome ")
else:
    print("It's not a palindrome ")
