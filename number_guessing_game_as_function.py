#!/usr/bin/env python 3.7

import random     #Importing the Random module which will generate numbers based on a range provided by the developer/programmer

hidden_number = random.randint(1, 111) # The variable named hidden_number assigned random integers between 1 and 111

attempts = 0 # Counter that will be incremented through each iteration

user_number = int(input("\nEnter your number: ")) # Variable named user_number will be assigned an integer entered by the game player in response to the prompt
while (user_number != hidden_number): # while loop tha checks for the user's number to match the random hidden number
     if user_number > hidden_number: # if user's number is to low they will be prompted for a higher number
         print("Lower") # if user's number is to high they will be prompted for a lower number
     else:
         print("Higher") # if user's number is to low they will be prompted for a higher number
     attempts += 1
     user_number = int(input("Enter your number: ")) 
print("Equal") # if user's number is a match they will receive a message stating they entered the Equal number.
#print("Congrats you entered the correct and equal number and it took you" attempts "attempts!")
print("\nCongrats you entered the correct and equal number in " + str(attempts) + " attempts!")
