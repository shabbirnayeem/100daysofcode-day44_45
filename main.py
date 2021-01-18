from tkinter import *
from tkinter import messagebox
import random
# it will copy text to the clip board
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_sym = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_sym + password_num
    random.shuffle(password_list)
    password = "".join(password_list)

    # enter the randomly generated password into the pass filed
    pass_input.insert(END, password)
    # this will copy the password into clipboard after the password is generated
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# The Add button going to use the save() method
# when you press the Add button its going to add save the data to the Data.txt file
# 1/17/2020, updating file format to json
# Adding error handling


def save():
    # Getting the user input from the entry using the get method
    web = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    # write data to a json file we need to create a dict of data
    new_data = {
        web: {
            "Email": email,
            "Password": password
        }
    }

    # the len function is going to check is the users left the web or the pass field empty
    # If it empty it will warn the user using messagebox.showwarning
    if len(web) == 0 or len(password) == 0:
        messagebox.showwarning(title="Ops", message="Please don't leave any files empty!")
    else:

        # After the user enters all the info, a message box will popup and show them the info to verify
        proceed = messagebox.askokcancel(title=web, message=f"Summary:\n Email:{email}\n Password:{password}\n "
                                                            f"Do you want to proceed?")

        # The message boc produces boolean Tru or False
        # If statement check if user click candle it bring the user back to the editor, else if saves the password
        if proceed:
            # Opening a file and appending the new account info to a new row

            try:
                # Going update the file type to a json file using the json library
                with open("Data.json", "r") as data_file:
                    # Reading old data using json.load(), it takes the name of the file
                    data = json.load(data_file)

            # If the file doesn't exit create new file
            except FileNotFoundError:
                with open("Data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            # if no error continue running the code
            else:
                # Updating the old data with new data using json.update()
                data.update(new_data)

                # write the new data to the json file
                # it basically reads the old data, updates the new data and write the new data
                with open("Data.json", "w") as data_file:
                    # First entry: the data you want to enter
                    # Second entry: the data you wanna write to
                    # Optional: indent the lines to make it easier to read
                    json.dump(data, data_file, indent=4)

            # Finally delete data from the entry
            finally:
                # Tkinter delete method will delete the text from each entry after we click add
                # starts from index 0 to END
                web_input.delete(first=0, last=END)
                # email_input.delete(first=0, last=END)
                pass_input.delete(first=0, last=END)


# ------------------------------------- FIND PASSWORD ------------------------------------------------------ #

# Function going to search for a password in the Data.json file


def find_password():
    web = web_input.get()

    try:
        with open("Data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR", message="No Data File Found")
    else:
        if web in data:
            email = data[web]['Email']
            password = data[web]["Password"]
            messagebox.showinfo(title=web, message=f"Email: {email},\n Password: {password}")
        else:
            messagebox.showwarning(title="ERROR", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# Adding padding
window.config(padx=50, pady=50)

# Tkinter Canvas
canvas = Canvas(height=200, width=200)

# read the image from the image file using Photoimage
image = PhotoImage(file="logo.png")

# create the image in the center
canvas.create_image(100, 100, image=image)

# Layout Manager
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
web_input = Entry(width=35)
web_input.grid(column=1, row=1)
web_input.focus()
email_input = Entry(width=54)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, string="test@gmail.com")
pass_input = Entry(width=35)
pass_input.grid(column=1, row=3)

# Button
# Creating the Generate Button
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
# Creating the Add Button
add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)
# Creating the Search Button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
