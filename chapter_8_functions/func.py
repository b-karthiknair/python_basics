import dict_mod as dm

def get_fruit_list(*args):
    # args is a tuple
    # list(args) converts the tuple into a list
    return list(args)

def freliminator(fruits):
    for index, fruit in enumerate(fruits):
        if fruit.lower()[0] == "a":
            del fruits[index]

if __name__ == "__main__":
    fruits = get_fruit_list("apple", "orange", "grape", "banana")

    print("fruits before:", fruits)
    #! this passes the list by reference
    freliminator(fruits=fruits)
    print("fruits after:", fruits)

    fruit_dict = dm.get_fruit_dict(fruits=fruits)
    dm.dict_mod(fruit_dict)
    print(fruit_dict)
