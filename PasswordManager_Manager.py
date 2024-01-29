"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    The part of the program contains all the functions for error checking, adding the passwords to a file, and finding passwords already in the manager.

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

import os

# Error check the password manager entried
def errorCheck(accountName, userName, password):
    if accountName == "" or userName == "" or password == "":
        print("Error")
        return False
    else:
        print("Success")
        return True

def passwordManager(accountName, userName, password):
    accounts = [[]] # Create the array that stores all the accounts

    # Add the account information to the array that was just created
    accounts[0].append(f"Account: {accountName}")
    accounts[0].append(f"User Name: {userName}")
    accounts[0].append(f"Password: {password}")

    print(accounts) # Print what was added to the terminal for programmer reference

    # Open then write the account information to the file
    with open('savedpasswords.txt', 'a') as savedpasswords:
        for i in range(0, len(accounts)):
            for a in accounts[i]:
                savedpasswords.write(f"{a}\n")
            savedpasswords.write("\n")

# Error check to see if the search field is filled out
def searchErrorCheck(accountInfo):
    if accountInfo == "":
        print("Error")
        return False
    else:
        print("Success")
        return True

# Search for the account that the user inputs
def search(accountInfo):
    accountFile = open('savedpasswords.txt', 'r') # Open the file that contains the account
    accountFileLines = [] # Create an array to store the file line in
    for line in accountFile: # Add the file lines to the array
        newLine = line.strip('\n') # Make sure the \n doesn't get added when the file lines are converted to strings in arrays
        accountFileLines.append(newLine)

    print(len(accountFileLines))
    
    with open('retrievedaccount.txt', 'w') as ra:
        # Check if there is anything in the password manager
        # If there is, then go through the password manager to find the account that matches
        # If not then display an error message
        if os.path.getsize("savedpasswords.txt") > 0:
            for i in range(0, len(accountFileLines) - 3):
                account = "Account: " + accountInfo
                # Check if the account matches
                if account == accountFileLines[i]:
                    # Write the found account to the text file
                    ra.write(f"{accountFileLines[i]}\n")
                    ra.write(f"{accountFileLines[i+1]}\n")
                    ra.write(f"{accountFileLines[i+2]}\n")
                    ra.write(f"{accountFileLines[i+3]}\n")
                    return "Success"
                # If the for loop has reached the end of the file and there is nothing in the retrievedccount.txt file, then the accunt doesn't exist
                elif i == (len(accountFileLines) - 4) and os.path.getsize("retrievedaccount.txt") == 0:
                    return "Nothing found"
        else:
            return "No accounts"
    
    accountFile.close() # Close the file with the stored accounts