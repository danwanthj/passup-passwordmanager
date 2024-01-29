"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    This part of the program generates a password, but only if the user wants to generate a strong password.

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

import random
import string
import PasswordManager_StrengthChecker as sc

def passwordGenerator():
    # Set the minimum length
    length = 12
    
    # Create the string that will store the charcters that are generated
    characterList = ""
    characterList += string.ascii_letters # Adding letters to the character list
    characterList += string.digits # Add numbers to to the character list
    characterList += string.punctuation # Add special characters to the character list

    # Create the array for the password `
    passwordArray = []

    for i in range(length): # Makes a 12 character password
        pickChar = random.choice(characterList) # Pick a random character from the character list
        passwordArray.append(pickChar) # Add the character to the password array

    # Convert the list to a string
    password = ""
    for c in passwordArray:
        password += c

    # Strength check the generated password, else run the function again
    strength = sc.strengthCheck(password) # Check the strength of the password that is generated
    if strength == "Strong" or strength == "Very Strong": # Make sure the password is strong
        return password
    else:
        passwordGenerator()