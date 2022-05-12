#!/usr/bin/env/python3.7

num_value = int(input("Please enter a numerical value between 0 and 100:   ")) #Initializing the variable num_value as an interger and prompting the user for a numberical value between 0 and 100

if ((num_value<0) or (num_value>100)):
    print("Please try again")
    num_value = int(input("Please enter a numerical value between 0 and 100:   ")) #Initializing the variable num_value as an interger and prompting the user for a numberical value between 0 and 100
    #continue

#counter = 0 # Counter is used for incorrect entries, if the user fails to enter a correct value 3 attempts then the program will exit.


if ((num_value>=90) and (num_value<=100)): #Grade comparisions going in descending order from 100 to 0, this line comment is for this group of if_else_elif statements
          print('\nYour grade is an A, Great job!!!')
elif ((num_value>=80) and (num_value<=89)):
          print('\nYour grade is an B, You did a wonderful job!!!')
else:
     if ((num_value>=70) and (num_value<=79)):
          print('\nYour grade is an C, Very good!!!')
if ((num_value>=60) and (num_value<=69)):
        print('\nYour grade is an D, Keep trying!!!')
elif ((num_value>=0) and (num_value<=59)):
    print('\nYour grade is an F, Please see me after class!!!')
    
print("\nGoodbye")