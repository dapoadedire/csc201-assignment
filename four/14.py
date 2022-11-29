myDictionary = {
    "name": "John",
    "age": 36,
    "country_of_birth": "United States",
    "favorite_language": "Python",
}


def findKey(key, dictionary):
    if key in dictionary:
        print("My", key, "is", dictionary[key])
    else:
        print("That key does not exist.")


findKey("name", myDictionary)
