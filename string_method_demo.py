# Validate user input
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

input = input("Enter a username: ")

if len(input)>12:
    print("Username should not be more than 12 characters")
elif input.count(' ')>0:
    print("Username should not contain spaces")
elif (input.isalnum() and (not input.isalpha())) or input.isdigit():
    print("Username should not contain digits")
else:
    print(f"Welcome {input}")