days = {
    "Sunday": "Aiku",
    "Monday": "Aje",
    "Tuesday": "Isegun",
    "Wednesday": "Ojoru",
    "Thursday": "Ojobo",
    "Friday": "Eti",
    "Saturday": "Abameta",
}

english_day = input("Input English Day: ")

try:
    african_language_day = days[english_day]
    print(african_language_day)
except:
    print("Error.")
