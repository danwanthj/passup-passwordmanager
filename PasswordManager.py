"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    This program takes all the functions defined outside this file and creates a password manager, generator, and strength checker all in one. All of these functions are used to create a password manager that is displayed using the tkinter GUI. 

Assignment Information
    Assignment:     Individual Project
    Author:         Danwanth Jeyakumar, djeyakum@purdue.edu
    Team ID:        LC3 - 19

Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import tkinter as tk
from tkinter import messagebox as mb
from tkmacosx import Button # For functions of the Button function that are available on windows but don't work on Mac
import PasswordManager_Manager as m
import PasswordManager_Generator as g
import PasswordManager_StrengthChecker as sc

def main():
    # Create the window
    root = tk.Tk() # Creates the window
    root.title("PassUp Password Manager") # Title for the window
    root.geometry("1000x920") # Size the window
    root.configure(bg="#000000") # Configure the window with a black background color
    root.resizable(False, False) # Make sure the window isn't resizable

    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file="passup-logo-notext.png")) # Set an app icon

    # Create a non-editable, scrollable window to display the saved passwords text file
    accountsList = tk.Text(root, width=75) # Create the textbox that will display the accounts that are added to the password manager
    accountsList.grid(column=2, row=1, rowspan=14, pady=25, padx=(25,100)) # Position the textbox so that it is on the right half of the screen and centered horizontally
    scrollbar = tk.Scrollbar(root, command=accountsList.yview) # Create the scroll widget
    scrollbar.grid(column=3, row=1, rowspan=8, sticky="nsew", pady=(42.5, 0)) # Position the scroll widget accordingly to the window
    accountsList['yscrollcommand'] = scrollbar.set # Allow the window to be scrolled using the scroll widget

    # Create the app title
    passwordManagerLabel = tk.Label(root, text="PASSUP", font="Dosis 24 bold", fg="#EBD99F", bg="#000000") # App title
    passwordManagerSubtitleLabel = tk.Label(root, text="A SIMPLE PASSWORD MANAGER", font="Dosis 16 bold", fg="#FFFFFF", bg="#000000") # App slogan/subtitle
    passwordManagerLabel.grid(column=0, row=0, padx=25, pady=(25, 5), columnspan=2) # Position app title
    passwordManagerSubtitleLabel.grid(column=0, row=1, padx=25, pady=(5, 25), columnspan=2) # Position app slogan/subtitle

    # Create the title for the Password Manager section
    addAccountLabel = tk.Label(root, text="ADD ACCOUNTS", font="Dosis 18 bold", fg="#EBD99F", bg="#000000") # Section for password manager title
    addAccountLabel.grid(column=0, row=2, padx=25, pady=(25, 0), columnspan=2) # Position the section title
    # Account Entry
    accountEntryLabel = tk.Label(root, text="ACCOUNT", font="Dosis 14", fg="#FFFFFF", bg="#000000") # Create the label for the first entry: Account
    accountEntryLabel.grid(column=0, row=3, padx=(25,0), pady=(25,0)) # Position the label
    accountEntry = tk.Entry(root, font="Dosis 14", fg="#FFFFFF") # Create the entry box for the first entry: Account
    accountEntry.grid(column=1, row=3, padx=25, pady=(25,0)) # Position the entry box
    # User Name Entry
    userNameEntryLabel = tk.Label(root, text="USERNAME", font="Dosis 14", fg="#FFFFFF", bg="#000000") # Create the label for the second entry: User Name
    userNameEntryLabel.grid(column=0, row=4, padx=(25,0), pady=(5,0)) # Position the label
    userNameEntry = tk.Entry(root, font="Dosis 14", fg="#FFFFFF") # Create the entry box for the second entry: User Name
    userNameEntry.grid(column=1, row=4, padx=25, pady=(5,0)) # Position the entry box
    # Password Entry
    passwordEntryLabel = tk.Label(root, text="PASSWORD", font="Dosis 14", fg="#FFFFFF", bg="#000000") # Create the label for the third entry: Password
    passwordEntryLabel.grid(column=0, row=5, padx=(25,0), pady=(5,0)) # Position the label
    passwordEntry = tk.Entry(root, font="Dosis 14", fg="#FFFFFF") # Create the entry box for the third entry: Password
    passwordEntry.grid(column=1, row=5, padx=25, pady=(5,0)) # Position the entry box
    # Create the function which the password manager button executes
    def callPasswordManager():
        accountName = accountEntry.get() # Get the account name from user entry
        userName = userNameEntry.get() # Get the user name from user entry
        password = passwordEntry.get() # Get the password from user entry
        # Error checking to check if any fields are empty in the password manager
        if m.errorCheck(accountName=accountName, userName=userName, password=password):
            m.passwordManager(accountName=accountName, userName=userName, password=password) # Call the password manager function
            mb.showinfo(title="Success!", message="Account Added!", icon="info") # Show the user that the account was added
            accountsList.insert("insert", "\n") # After they click ok, add some whitespace
            with open("savedpasswords.txt", "r") as f: # Read the file and write into the textbox
                accountsList.delete("1.0", "end") # Clear the textbox before adding the entire file, else there will be duplicates
                accountsList.insert("insert", f.read()) # Insert the file contents into the textbox
                accountsList.config(padx=25, pady=25) # Format how the textbox looks
            # Delete the entry boxes
            accountEntry.delete(0, "end")
            userNameEntry.delete(0, "end")
            passwordEntry.delete(0, "end")
        else:
            mb.showinfo(title="Something's wrong…", message="One or more of the fields are empty…", icon="warning") # Show the user that there is an error
    # Display the original selection of accounts before the user adds anything
    with open("savedpasswords.txt", "r") as f: # Open the file and read it
            accountsList.insert("insert", f.read()) # Add the file contents to the textbox
            accountsList.config(padx=25, pady=25) # Format how the textbox looks
    # Button to Submit Information
    submitAccountInfoButton = Button(root, text="SUBMIT", font="Dosis 14 bold", fg="#000000", bg="#EBD99F", padx=100, pady=5, borderless=1, activebackground="#8E6F3E", command=callPasswordManager) # Button to submit information; fires the callPasswordManager() function
    submitAccountInfoButton.grid(column=0, row=6, columnspan=2, padx=25, pady=(10, 0)) # Position the button

    # Create the search bar in the password manager
    searchLabel = tk.Label(root, text="SEARCH FOR ACCOUNTS", font="Dosis 18 bold", fg="#EBD99F", bg="#000000") # Create the title for the search section
    searchLabel.grid(column=0, row=7, columnspan=2, padx=(25,0), pady=(50,0)) # Position the title
    searchBarEntryLabel = tk.Label(root, text="ACCOUNT", font="Dosis 14", fg="#FFFFFF", bg="#000000") # Create a label for the entry: Account Name
    searchBarEntryLabel.grid(column=0, row=8, padx=(25,0), pady=(25,0)) # Position the label
    searchBarEntry = tk.Entry(root, font="Dosis 14", fg="#FFFFFF") # Create the entry box
    searchBarEntry.grid(column=1, row=8, padx=25, pady=(25,0)) # Position the entry box
    # Create the function which the search button executes
    def searchForAccount():
        accountInfo = searchBarEntry.get()
        value = m.search(accountInfo) # Get the user entry for account name, and call the search function at the same time
        # Error checking to check if there is an empty field
        if m.searchErrorCheck(accountInfo=accountInfo):
            if value == "Success": # If the account is found
                mb.showinfo(title="Success!", message="Account retrieved!", icon="info") # Show an alert to the user that the account was found in the list
                # Create a pop-up window
                top = tk.Toplevel(root) # Create the window
                top.geometry("500x300") # Define the sixe
                top.configure(bg="#000000") # Set a background color
                top.resizable(False, False) # Make sure it can't be resized
                top.title("Search Results") # Create the title for the window
                searchResults = tk.Text(top, height=50) # Create the textbox where the search results will be displayed
                searchResults.pack() # Position the textbox
                scrollbar2 = tk.Scrollbar(top, command=searchResults.yview) # Create a scroll widget to make the texbox scrollable just in case there are multiple accounts with the same name
                scrollbar2.pack() # Position the scroll widget
                searchResults['yscrollcommand'] = scrollbar2.set # Make the window scrollable
                with open("retrievedaccount.txt", "r") as f: # Open the file where the searched information is stored
                    searchResults.insert("insert", f.read()) # Write to the textbox
                    searchResults.config(padx=25, pady=25) # Format the textbox
                searchBarEntry.delete(0, "end") # Delete the entry from the entry box
                searchResults.config(state="disabled") # Make sure the textbox is not editable
            elif value == "Nothing found": # If no account is found
                mb.showinfo(title="No account found", message="Nothing found. Check your search input or add an account using the password manager.", icon="warning")
            elif value == "No accounts": # If the password manager has no saved accounts
                mb.showinfo(title="Something's wrong…", message="There's nothing in the password manager yet! Add some accounts!", icon="warning")
        else:
            mb.showinfo(title="Something's wrong…", message="The field is empty…", icon="warning")
    # Button to search
    searchButton = Button(root, text="SEARCH", font="Dosis 14 bold", fg="#000000", bg="#EBD99F", padx=100, pady=5, borderless=1, activebackground="#8E6F3E", command=searchForAccount) # Button that fires the searchForAccount() function
    searchButton.grid(column=0, row=9, columnspan=2, padx=25, pady=(10, 0)) # Position the button

    # Create the password generator
    passwordGeneratorLabel = tk.Label(root, text="PASSWORD GENERATOR", font="Dosis 18 bold", fg="#EBD99F", bg="#000000") # Create the title for the password generator section
    passwordGeneratorLabel.grid(column=0, row=10, columnspan=2, padx=(25, 0), pady=(50, 0)) # Position the title
    # Function that the password generator executes
    def generatePassword():
        generatedPassword = tk.Label(root, text=g.passwordGenerator(), font="Dosis 14 bold", fg="#EBD99F", bg="#000000") # Make the label that shows the password on screen
        generatedPassword.grid(column=1, row=12, padx=25, pady=(0, 0)) # Position the label
        mb.showinfo(title="Success!", message="Password generated!", icon="info") # Show an alert that the password has been generated
    # Button to generate password
    passwordGeneratorButton = Button(root, text="GENERATE", font="Dosis 14 bold", fg="#000000", bg="#EBD99F", padx=100, pady=5, borderless=1, activebackground="#8E6F3E", command=generatePassword) # Button that fires the generatePassword() function
    passwordGeneratorButton.grid(column=0, row=11, columnspan=2, padx=25, pady=25) # Position the button
    # Display Password
    generatedPasswordLabel = tk.Label(root, text="YOUR PASSWORD", font="Dosis 14", fg="#FFFFFF", bg="#000000") # Create the label that signifies where the generated password is
    generatedPasswordLabel.grid(column=0, row=12, padx=(25, 0), pady=(0, 0)) # Position the label

    # Create the password strength checker
    passwordStrengthCheckerLabel = tk.Label(root, text="STRENGTH CHECKER", font="Dosis 18 bold", fg="#EBD99F", bg="#000000") # Create the title for the strength checker section
    passwordStrengthCheckerLabel.grid(column=0, row=13, columnspan=2, padx=(25, 0), pady=(50, 25)) # Position the title
    # Function that the password generator executes
    def passwordStrengthCheck():
        password = strengthCheckerEntry.get() # Get the entry from the user entry
        if sc.strengthErrorCheck(password) == "Error":
            mb.showinfo(title="Something's wrong…", message="The field is empty…", icon="warning")
        elif sc.strengthErrorCheck(password) == "Password not long enough":
            mb.showinfo(title="Error!", message="Your password is not long enough! Make sure it's at least 11 characters!", icon="warning")
        else:
            strength = sc.strengthCheck(password) # Call the strength checker function
            mb.showinfo(title="Alert!", message=("Password strength: " + strength), icon="info") # Show an alert notifying the user about their password strength
            strengthCheckerEntry.delete(0, "end") # Clear the entry field
    # Entry for the password that needs to be checked
    strengthCheckerLabel = tk.Label(root, text="PASSWORD", font="Dosis 14", fg="#FFFFFF", bg="#000000") # Make the label for the entry box
    strengthCheckerLabel.grid(column=0, row=14, padx=(25,0), pady=(5,0)) # Position the label
    strengthCheckerEntry = tk.Entry(root, font="Dosis 14", fg="#FFFFFF") # Make the entry box
    strengthCheckerEntry.grid(column=1, row=14, padx=25, pady=(5,0)) # Position the entry box
    # Button to check the password
    strengthCheckerButton = Button(root, text="CHECK", font="Dosis 14 bold", fg="#000000", bg="#EBD99F", padx=100, pady=5, borderless=1, activebackground="#8E6F3E", command=passwordStrengthCheck) # Button that fires the passwordStrengthCheck() function
    strengthCheckerButton.grid(column=0, row=15, columnspan=2, padx=25, pady=(10, 25)) # Position the button

    root.mainloop() # Make sure everything is displayed in a window

if __name__ == "__main__":
    main()