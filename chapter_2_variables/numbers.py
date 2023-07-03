# When you divide any two numbers, even if they are integers that result in a
# whole number, you’ll always get a float
print(4 / 2)  # Output: 2.0

# When you’re writing long numbers, you can group digits using underscores
# to make large numbers more readable
micro = 1_000_000
milli = micro / 1000
print("milli:", milli)  # Output: 1000.0

# Demonstrating multiple assignments
a, b, c = 10, 20, 30
print(a, b, c)  # Output: 10 20 30

# Using all capital letters for constants
PI = 3.14_15
print(PI ** 2)  # Output: 3.1415 ^ 2 (squared)

try:
    # Attempting to alter the value of a constant (which is just a convention, unlike C/C++)
    PI /= 3
    print("Constants being altered does not throw an error. It is just a convention, unlike C/C++.")
except:
    print("An exception occurred")
