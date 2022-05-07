#!/usr/bin/bash env python3.7
# Program can be executed from a Python CLI

l = float(input("Enter the length:   ")) #Used float to account for non-interger numbers
w = float(input("Enter the width:    "))


sq_feet = (l * w) # Multiplying the length and the width to obtain the square footage of the room

print("The Square Footage of the room as a floating number is:" + (str(sq_feet))) #Displaying the total square footage as a floating numberr

sq_feet_int = int(sq_feet) # Multiplying the length and the width to obtain the square footage of the room

print("The Square Footage of the room as an integer number is:" + (str(sq_feet_int))) #Displaying the total square footage as an integer number