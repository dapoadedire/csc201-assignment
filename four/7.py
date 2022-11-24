months_dictionary = {
    "January": "Oṣù Ṣẹ̀rẹ́",
    "February": "Oṣù Èrèlè",
    "March": "Oṣù Ẹrẹ̀nà",
    "April": "Oṣù Ìgbé",
    "May": "Oṣù Ẹ̀bìbì",
    "June": "Oṣù Òkúdu",
    "July": "Oṣù Agẹmọ",
    "August": "Oṣù Ògún",
    "September": "Oṣù Ọ̀wẹwẹ",
    "October": "Oṣù Ọ̀wàrà",
    "November": "Oṣù Bélú",
    "December": "Oṣù Ọ̀pẹ́",
}

english_month = input("Input English Month: ")

try:
    african_language_month = months_dictionary[english_month]
    print(african_language_month)
except:
    print("Error.")