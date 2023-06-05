# Encrypted Password Manager

This is a password manager application which provides a secure way to store passwords. This application uses the tkinter library for its graphical user interface and the cryptography library to securely store passwords.

## Features

- **Password Encryption**: Passwords are encrypted using the Fernet encryption method from the cryptography library, ensuring that they are not easily readable if the data file is accessed without the application.
- **Local Storage**: Encrypted passwords are stored locally in a JSON file, which is a lightweight and widely used data-interchange format that is easy to read and write.
- **UI**: This password manager uses a graphical user interface (GUI) made with the tkinter library to make it user friendly and easy to use.

## Requirements

This project requires Python 3, as well as the following Python libraries:

- tkinter
- pyperclip
- json
- cryptography
- bcrypt

You can install these libraries using pip:

```bash
pip install tk
pip install pyperclip
pip install cryptography
pip install bcrypt
```
## Setup

Before running the main password manager script, you need to generate a key for the encryption and a password to unlock the manager.

- **Key**: Run the **'key.py'** script to create a **'key.key'** file, which will be used to encrypt and decrypt your passwords. This key will be automatically generated and stored in a file named key.key.
- **Password**: Run the **'password.py'** script to create a hashed password that will be used to unlock the password manager. You'll be prompted to enter a password, which will be hashed and stored in a file or in the code.

After running these scripts and setting up the key and password, you're ready to start using the password manager!

## Usage 

To start the password manager, run the main script. You'll be asked to enter the password that you set up. If the password is correct, you'll be able to add, view, and manage your passwords.

Please note that you should keep your **'key.key'** file and hashed password secure, as anyone with access to these would be able to decrypt your passwords.

## Conclusion

This password manager provides a simple and secure way to manage your passwords. The application encrypts passwords and stores them locally, ensuring that your passwords remain secure and accessible only to you.
