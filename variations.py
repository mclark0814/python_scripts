#!/usr/bin/env python3.7

# Python implementation here

message = input("Enter a message: ")

print("Lowercase:", message.lower())

print("Uppercase:", message.upper())

print("Capitalize:", message.capitalize())

print("Title Case:", message.title())

words = message.split()

print("words:", words)

sorted_words = sorted(words)

print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])

