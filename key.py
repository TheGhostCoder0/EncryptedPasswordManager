# This script is used to generate a key for the encryption and decryption
# of passwords in the password manager.

from cryptography.fernet import Fernet

# Generate a new key using the Fernet method from the cryptography library.
key = Fernet.generate_key()

# Open the key file in write mode and save the generated key. 
# If the key file does not exist, it will be created.
with open('key.key', 'wb') as key_file:
    key_file.write(key)
