#!/usr/bin/env python3.7

message = input("Enter a message: ") # Prompting user to input a message

print("First character:", message[0]) # Output shows the first character of the message
print("Last character:", message[-1]) # Output shows the last character of the message
print("Middle character:", message[int(len(message) / 2)]) # Output shows the middle character of the message
print("Even index characters:", message[0::2]) # Output shows the even character of the message
print("Odd index characters:", message[1::2]) # Output shows the odd character of the message
print("Reversed message:", message[::-1]) # Output shows the characters of the message in reverse order