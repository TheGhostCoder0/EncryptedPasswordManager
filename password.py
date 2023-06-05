import bcrypt

password = "PASSWORD".encode()  # TODO: Replace "your_password" with your actual password
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)  # Print the hashed password
