#!usr/bin/env python3.7

users = [] # Empty users list

assert users == [], f"Expected 'users' to be [] but got: {repr(users)}"  # Empty users list

# appending 3x user names to the list
users.append('kevin') 
users.append('bob')
users.append('alice')

# Generates lists showing 3x users from te above users.append functions
assert users == ['kevin', 'bob', 'alice'], f"Expected 'users' to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

del users[1] # Delete 1 user's name from the list
assert users == ['kevin', 'alice'], f"Expected 'users' to be ['kevin', 'alice'] but got: {repr(users)}"

rev_users = list(reversed(users)) # List the users in reversed order
assert rev_users == ['alice', 'kevin'], f"Expected 'rev_users' to be ['alice', 'kevin'] but got: {repr(rev_users)}"

users.insert(1, 'melody') # Insert one user's name into the list
assert users == ['kevin', 'melody', 'alice'], f"Expected 'users' to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

users += ['andy', 'wanda', 'jim'] # Add and append 3x new user names to the list

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected 'users' to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

center_users = users[2:4] # List the two user's names in the middle of the list
assert center_users == ['alice', 'andy'], f"Expected '_users' to be ['alice', 'andy'] but got: {repr(center_users)}"