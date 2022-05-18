#!/usr/bin/env python3.7
import random

def random_string_id(chunk_amount = 4, chunk_size = 4):
    lower_letters = [chr(i) for i in (range(ord("a"),ord("z")+1))]
    numbers = [str(i) for i in range(0,10)]
    characters = lower_letters + numbers

number = random.randint(0,100)



#print(number) # print random number 0 - 99

#letter = chr(random.randint(ord("A"),ord("Z")))

capital_letter = [chr(range(ord("A"),ord("Z")+1))]


capital_letters = [chr(i) for i in (range(ord("A"),ord("Z")+1))]
lower_letters = [chr(i) for i in (range(ord("a"),ord("b")+1))]


letters = capital_letters + lower_letters

#print(random.choice(letters))

