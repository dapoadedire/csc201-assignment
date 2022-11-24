dictionary = {
    "Big": "Elephant",
    "Small": "Mouse",
    "Fast": "Cheetah",
    "Slow": "Turtle",
    "Strong": "Lion",
    "Tall": "Giraffe",
}

def sort_by_value(dictionary):
    sorted_dictionary = {}
    sorted_keys = sorted(dictionary, key=dictionary.get)
    for key in sorted_keys:
        sorted_dictionary[key] = dictionary[key]
    return sorted_dictionary


print(sort_by_value(dictionary))