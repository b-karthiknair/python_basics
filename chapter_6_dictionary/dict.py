"""
* A dictionary in python is a collection of key-value pairs
* the key value pairs are enclosed in curly brackets
"""

car = {"colour": "green", "model": "jazz", "year": 2009}
print("colour:", car["colour"])

# starting with an empty dict
car = {}
car["colour"] = "orange"
print("colour:", car["colour"])

# get()
# * the following line will cause an error
# top_speed = car['top_speed']
# * this doesn't
top_speed = car.get("top_speed")
print("top speed:", top_speed)

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

# iterating a dict
for key, value in user_0.items():
    if(value == "fermi"):
        print(f"\nfound an identity with the {key} name as {value.title()}")

print("the fields checked were:")
for key in user_0:
    print("\t",key)

#* OR
print("\nthe fields checked were:")
for key in user_0.keys():
    print("\t",key)

print("\nthe fields checked were (sorted):")
for key in sorted(user_0):
    print("\t",key)