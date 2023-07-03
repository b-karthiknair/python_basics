# A list is a collection of items in a particular order. It can include various data types.

# Creating a list of names
names = ["Xavi", "Iniesta", "Sergio"]
print("\nMidfield trio:", names)

# Accessing the last element in the list
print("Last name in the list:", names[-1])

# Using an f-string to create a message
message = f"{names[0].title()} has retired. We need to replace him."
print(message)

# Modifying an element in the list
names[0] = "Ivan Rakitic"
print("Midfield trio:", names)

# Adding an element to the end of the list using append()
names.append("Sergi Roberto")

# Inserting an element at a specific position using insert()
names.insert(3, "Thiago Alcantara")
print("Midfield lineup:", names)

# Removing an element from the list using pop()
names.pop(3)
print("Midfield lineup after pop:", names)

# Removing multiple elements from the list using del
del names[0:2]
print("Midfield lineup:", names)

# Removing an element when the index is unknown using remove()
names.insert(1, "Pedri Gonzalez")
names.append("Pedri Gonzalez")  # Adding the same name again
names.remove("Pedri Gonzalez")  # Removing the first occurrence
print("Midfield lineup:", names)

# Sorting the list in ascending order
names.sort(reverse=False)
print("Midfield lineup:", names)

# Sorting the list using the sorted() function (does not alter the original list)
sorted_names = sorted(names, reverse=True)
print("\nMidfield lineup:", names)  # Original list remains unchanged
print("Midfield lineup (sorted):", sorted_names)

# Reversing the order of the list using the reverse() function
names.reverse()
print("Midfield lineup (reversed):", names)

# Getting the length of the list using len()
print("Number of midfielders:", len(names))

# Iterating the list
for midfielder in names:
    print("\t", midfielder)