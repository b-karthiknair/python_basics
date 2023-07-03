series = [value for value in range(1, 3)]
print(series)

if 1 in series:
    print(1, "found!")

if 3 not in series:
    print(3, "not found!")

# checking for empty list
test_list = []
if not test_list:
    print("found test_list as empty")
else:
    print("found test_list as not empty")
