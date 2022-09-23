#######################################
# IT 2750 - Lab 02                    #
# Generate a secure password          #
# Author: Tim Kurash                  #
# S#: S01284480                       #
#######################################

# Import libraries needed for this lab
from math import log2
import random
import string

# Define a method generatePassword that:
# - Has the following parameters:
#   + length -> int, length of password to be created
#   + upper -> bool, True means include uppercase letters, False means
#              do not include uppercase letters
#   + lower -> bool, True means include lowercase letters, False means
#              do not include lowercase letters
#   + numbers -> bool, True means include numbers, False means
#                do not include numbers
#   + symbols -> bool, True means include symbols, False means
#                do not include symbols
def generatePassword(length, upper, lower, numbers, symbols):
    # Create local variables for the set of characters that can be used
    # and the new password that will be returned from the function
    chars = ""
    newPassword = ""

    # Don't allow creation of passwords < 6 characters
    if (length < 6):
        print("Password will not be secure enough, please choose at least 6 characters")
        getInput()

    # If user selects no character sets it should ask them to choose again.
    if (not upper) & (not lower) & (not numbers) & (not symbols):
        print("You need to select at least 1 character set")
        getInput()

    # Use if statements and the string.ascii_ constants to add the various
    # character sets to the local variable tracking what characters to be
    # used (https://docs.python.org/3/library/string.html, see "String 
    # constants" for reference)
    if upper:
        chars = chars + string.ascii_uppercase
    if lower:
        chars = chars + string.ascii_lowercase
    if numbers:
        chars = chars + string.digits
    if symbols:
        chars = chars + string.punctuation


    # Create a loop (of any type) to add a random character from the set of
    # characters (hint: using random.choice(...)) to the new password
    # placeholder variable

    for i in range(length):
        newPassword = newPassword + random.choice(chars)

    # Call getEntropy to calculate bits of entropy of generated password
    entropy = getEntropy(length,chars)

    # Return the new password and entropy as the function's return value
    return newPassword, entropy

def getEntropy(length, chars):
    # Calculate total number of combinations based on total number of characters and length of password
    possibleCombinations = int(len(chars) ** length)

    # Calculate bits of entropy
    entropy = log2(possibleCombinations)
    
    # Return entropy as return value
    return entropy

def getInput():


    # Ask the user how long of a password they want
    length = int(input("How many characters do you want the password to be (at least 6)?: "))

    # Ask the user if they want to use uppercase, lowercase, numbers
    # and symbols in separate input statements. Remember to properly
    # handle variable types! (hint: bool(...) converts to bool, 
    # int(...) converts to int, str(...) converts to string)
    upper = bool(int(input("Do you want UPPERcase letters? (1 for Yes/0 for No): ")))
    lower = bool(int(input("Do you want lowercase letters?(1 for Yes/0 for No)): ")))
    numbers = bool(int(input("Do you want numbers?(1 for Yes/0 for No): ")))
    symbols = bool(int(input("Do you want symbols?(1 for Yes/0 for No): ")))

    # Call the generatePassword function and pass in the user's choices
    # and display the return value to the user
    print('----------------------------------------------------')
    print('Generating password...')
    print('----------------------------------------------------')
    # Set newPassword and entropy variables to the return values of the generatePassword function
    newPassword, entropy = generatePassword(length, upper, lower, numbers, symbols)
    # Print out the generated password
    print("Your new password is: " + newPassword)
    # Print out the rounded bits of entropy
    print ("It has approximately", round(entropy, 2), "bits of entropy")
    print('====================================================')
    
    # Ask user if they want another password generated
    again = bool(int(input("\nWould you like another password generated (1 for Yes/0 for No): ")))
    
    # Call getInput if true, else exit out
    if again:
        getInput()
    else:
        print('\n====================================================')
        print('Thank you for using the Ultimate Password Generator!')
        print('====================================================')
        quit


# Print a welcome message
print('====================================================')
print('==== WELCOME TO THE ULTIMATE PASSWORD GENERATOR ====')
print('====================================================')
# Call getInput function at start of program
getInput()