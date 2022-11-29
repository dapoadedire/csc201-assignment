myDictionary = {
    "name": "John",
    "age": 36,
    "country of birth": "United States",
    "favorite language": "Python",
}


def findKey(key, dictionary):
    if key in dictionary:
        print("My", key, "is", dictionary[key])
    else:
        print("That key does not exist.")


findKey("name", myDictionary)
