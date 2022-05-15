#!/usr/bin/env python3.7

hidden_number = 25

for attempts in range(5):
    user_num = int(input("\nEnter a whole number: "))
    if (user_num == hidden_number):
        print("\nYou entered the correct and Equal number.", user_num)
        print("\nThanks for playing the Number guessing game, Goodbye!!!")
        break
        
    if (user_num < hidden_number):
        print("\nHigher, you entered: ", user_num)
    else:
        print("\nLower, you entered: ", user_num)
