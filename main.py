from tkinter import *
from tkinter import messagebox
import random
# it will copy text to the clip board
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_sym = [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_num = [random.choice(numbers) for char in range(nr_numbers)]

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
def save():
    # Getting the user input from the entry using the get method
    web = web_input.get()
    email = email_input.get()
    password = pass_input.get()

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
            with open("Data.txt", "a") as data_file:
                data_file.write(f"{web} | {email} | {password}\n")

            # Tkinter delete method will delete the text from each entry after we click add
            # starts from index 0 to END
            web_input.delete(first=0, last=END)
            # email_input.delete(first=0, last=END)
            pass_input.delete(first=0, last=END)

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
web_input = Entry(width=54)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()
email_input = Entry(width=54)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, string="Shabbir.Nayeem@gmail.com")
pass_input = Entry(width=35)
pass_input.grid(column=1, row=3)

# Button
# Creating the Generate Button
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
# Creating the Add Button
add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
