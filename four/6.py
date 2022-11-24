days = {
    "Sunday": "Aiku",
    "Monday": "Aje",
    "Tuesday": "Isegun",
    "Wednesday": "Ojoru",
    "Thursday": "Ojobo",
    "Friday": "Eti",
    "Saturday": "Abameta" 
}

english_day = input("Input English Day: ")

try:
    african_language_day = days["Sunday"]
    print(african_language_day)
except:
    print("Error.")