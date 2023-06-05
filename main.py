from tkinter import *
from tkinter import messagebox, simpledialog
from random import choice, randint, shuffle
import pyperclip
import json
from cryptography.fernet import Fernet
import bcrypt

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Helvetica", 14, "normal")
WHITE = "#ffffff"
BLACK = "#000000"
MOST_COMMON_EMAIL = "example@email.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- PASSWORD CHECK ------------------------------- #
# Hashed password to check against (You should create this securely and store it somewhere safe)
correct_password_hash = b'*********************************************************' # TODO: Set correct_password_hash to password.py hash


def password_check():
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    if bcrypt.checkpw(password.encode(), correct_password_hash):
        return True
    else:
        messagebox.showinfo(title="Error", message="Incorrect password")
        return False


# ---------------------------- Key Encrypt/Decrypt ------------------------------- #
try:
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)
except FileNotFoundError:
    messagebox.showinfo(title="Error", message="Encryption key file not found.")
    # You could exit the program here, or handle this error differently depending on your needs
except Exception as e:
    messagebox.showinfo(title="Error", message=f"Error initializing encryption: {str(e)}")
    # Handle any other error that may occur


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    encrypted_password = cipher_suite.encrypt(password.encode())

    new_data = {
        website: {
            "email": email,
            "password": encrypted_password.decode()
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Not all fields entered")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if len(website) != 0:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            if website in data:
                email = data[website]["email"]
                encrypted_password = data[website]["password"].encode()  # Get encrypted password
                password = cipher_suite.decrypt(encrypted_password).decode()  # Decrypt password
                messagebox.showinfo(title=website, message=f"Email/Username: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No Details for {website} exist")
        finally:
            website_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Error", message="No website provided")


# ---------------------------- UI SETUP ------------------------------- #
if password_check():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg=WHITE)

    # Logo
    logo_img = PhotoImage(file="logo.png")
    canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    # Labels
    website_label = Label(text="Website:", bg=WHITE, fg=BLACK, font=FONT)
    website_label.grid(row=1, column=0)

    email_user_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK, font=FONT)
    email_user_label.grid(row=2, column=0)

    password_label = Label(text="Password:", bg=WHITE, fg=BLACK, font=FONT)
    password_label.grid(row=3, column=0)

    # Entries
    website_entry = Entry(width=21, fg=BLACK, bg=WHITE, highlightthickness=0, insertbackground=BLACK)
    website_entry.focus()
    website_entry.grid(row=1, column=1, padx=1, pady=1)

    email_user_entry = Entry(width=39, fg=BLACK, bg=WHITE, highlightthickness=0, insertbackground=BLACK)
    email_user_entry.grid(row=2, column=1, columnspan=2, padx=1, pady=1)
    email_user_entry.insert(0, MOST_COMMON_EMAIL)

    password_entry = Entry(width=21, fg=BLACK, bg=WHITE, highlightthickness=0, insertbackground=BLACK)

    password_entry.grid(row=3, column=1, padx=1, pady=1)

    # Buttons
    search_button = Button(text="Search", fg=BLACK, bg=WHITE, highlightthickness=0,
                           highlightbackground=WHITE, width=14, command=find_password)
    search_button.grid(row=1, column=2, padx=1, pady=1)

    generate_password_button = Button(text="Generate Password", fg=BLACK, bg=WHITE, highlightthickness=0,
                                      highlightbackground=WHITE, command=generate_password, width=14)
    generate_password_button.grid(row=3, column=2)

    add_button = Button(width=37, text="Add", fg=BLACK, bg=WHITE, highlightthickness=0, highlightbackground=WHITE,
                        command=save_password)
    add_button.grid(row=4, column=1, columnspan=2)

    canvas.mainloop()
else:
    print("Wrong Password!")
