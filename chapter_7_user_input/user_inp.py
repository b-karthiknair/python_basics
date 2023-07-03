age = int(input("Enter your age: "))
try:
    print(f"You have {abs(round(100-age))} years to live")
except:
    print("Enter an integer value")