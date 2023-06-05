# This script is used to generate a hashed password using the bcrypt library.
# The hashed password is used to validate the user before providing access to the password manager.

import bcrypt

# Your password goes here (replace "PASSWORD" with your actual password).
# The password is encoded because the bcrypt.hashpw() function expects bytes.
password = "PASSWORD".encode()

# bcrypt.gensalt() generates a new random salt. This salt is used to hash the password.
# bcrypt.hashpw() then hashes the password using this salt. The result is a bytes object.
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# The hashed password is printed to the console.
# You should copy this hashed password and securely store it for later use.
print(hashed)  # Print the hashed password
