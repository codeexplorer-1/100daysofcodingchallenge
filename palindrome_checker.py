def is_palindrome(text):
  text = ''.join(char.lower() for char in text if char.isalnum())
  return text == text[::-1]
user_text = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_text):
  print(user_text, "is a palindrome!")
else:
  print(user_text, "is not a palindrome.")
