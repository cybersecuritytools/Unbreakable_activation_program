import os
from cryptography.fernet import Fernet
print("Welcome to activator")
print("")
type = input()
key = Fernet.generate_key
key_encrypt = Fernet.encrypt(key) 
if type == key_encrypt:
    print("Your program was sucefully activated!")
    breakpoint