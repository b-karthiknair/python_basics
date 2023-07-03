# This code is for experimenting with strings
# Functions and concepts used:
# * title()
# * upper()
# * lower()
# * islower()
# * f-strings
# * rstrip(), lstrip() and strip(): they do not remove whitespaces from the original string. Instead, they return a modified string

# Demonstrating the title() function
name = "ada lovelace"
print(name.title())  # Output: "Ada Lovelace"

# Demonstrating the upper() and lower() functions
name = "James Bond"
print(name.upper())  # Output: "JAMES BOND"
print(name.lower())  # Output: "james bond"

# Demonstrating the islower() function
name = "James Bond"
print(name.islower())  # Output: False

# Using f-strings
first_name = "Vladimir"
last_name = "Putin"
full_name = f" {first_name} {last_name} "  # Using f-string to concatenate names
print(full_name)
print(full_name.strip())  # Output: "Vladimir Putin" (removing leading and trailing whitespace)

# Uncomment the line below to see the effect of rstrip() on the right side of the string
# print(f"\n{full_name.rstrip()}")
