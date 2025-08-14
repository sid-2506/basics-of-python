# Message encryption and decryption
import string

chars = string.ascii_letters + string.digits + string.punctuation

input = input("Enter a message to encrypt or decrypt: ")

res = ""

for char in input:
    if char in chars:
        res+=chars[-chars.index(char)]
    else:
        res+=char
        
print(f"Final result : {res}")