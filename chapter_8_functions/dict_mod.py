def get_fruit_dict(fruits):
    fruit_dict = {}
    for index, fruit in enumerate(fruits):
        fruit_dict[fruit] = index + 1
    return fruit_dict

def dict_mod(test_dict):
    for key in test_dict:
        try:
            test_dict[key] *= 2
        except:
            pass


