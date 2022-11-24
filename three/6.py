score = input("Input your score")

if score > 70:
    grade = "A"
elif 60 <= score <= 69:
    grade = "B"
elif 50 <= score <= 59 :
    grade = "C"
elif 40 <= score <= 49:
    grade = "D"
elif 39 <= score <= 44:
    grade = "E"
else:
    grade = "F"


print(grade)