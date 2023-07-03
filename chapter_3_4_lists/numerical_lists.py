"""
Python List Operations

This code demonstrates various operations on Python lists, including:
- Creating lists using loops and list comprehensions
- Finding minimum, maximum, and sum of list elements
- Slicing lists
- Copying lists by reference and by value

"""

# Creating an empty list
list1 = []

# for value in range(6):
#     print(value)

# Populating list1 using a loop
for value in range(10, 20, 2):
    list1.append(value)

print("\nlist 1:", list1)  # Displaying list1
print("Some stats:")
print("\tmin:", min(list1))  # Finding the minimum value in list1
print("\tmax:", max(list1))  # Finding the maximum value in list1
print("\tsum:", sum(list1))  # Calculating the sum of values in list1

# Creating list2 using a list comprehension
list2 = [value for value in range(0, 10, 2)]
print("\nlist 2:", list2)  # Displaying list2
print("Some stats:")
print("\tmin:", min(list2))  # Finding the minimum value in list2
print("\tmax:", max(list2))  # Finding the maximum value in list2
print("\tsum:", sum(list2))  # Calculating the sum of values in list2

# Creating list3 using a list comprehension with squared values
list3 = [value**2 for value in range(1, 10, 2)]
print("\nlist 3:", list3)  # Displaying list3

# Slicing list3
list3 = list3[:4]
print("list 3 after slice:", list3)  # Displaying sliced list3

# More slicing examples
print("sliced 1:", list3[1:])  # Displaying a slice of list3 from index 1 to the end
print("sliced 2:", list3[-3:])  # Displaying a slice of the last 3 elements in list3

print("\nlist 3:", list3, "and list 4 is assigned list 3")
list4 = list3  # Copying list3 by reference
list4.pop()
print("list 3 after popping list 4:", list3)  # Displaying list3 after modifying list4

list4 = list3[:]  # Copying list3 by value using slicing
print("\nlist 3:", list3, "and list 4 is assigned list 3 (through slicing)")
list4.pop()
print("list 3 after popping list 4:", list3)  # Displaying list3 after modifying list4


# merging two lists
list4.extend(list3)
print("list 3 after popping list 4:", list4)  # Displaying list4 after modifying list4
