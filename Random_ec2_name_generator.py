#!/usr/bin/env python3.7

import random #Importing the Random module which will generate numbers based on a range provided by the developer/programmer

def ec2_name_chars(num_chars): #definition of function that the value assgned to num_char to generated a number of characters
    return "".join(chr(random.randint(33,125)) for i in range(num_chars))
    
ec2_count = int(input("Enter the number of AWS EC2 instances ")) # Counter that will be incremented through each iteration

count = 0

while count != ec2_count: # Counter that will be incremented through each iteration 
    if count < ec2_count:
        ec2_name = str(input("\nEnter the name of your AWS ec2 instance: "))  #Prompts the user for the desired named of the ec2 instance
        print(ec2_name + ec2_name_chars(15))  #Print statement presents both the requested name and the generated characters
        print("\n")
        count += 1
    elif count == ec2_count:
        ec2_name = str(input("\nEnter the name of your AWS ec2 instance: ")) #Prompts the user for the desired named of the ec2 instance
        
print("Your request has been completed") #Noifies the user that their request has been comppleted