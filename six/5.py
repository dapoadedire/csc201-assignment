class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses
        self.grades = self.compute_grades()
        self.points = self.compute_points()
        self.remarks = self.compute_remarks()
        
    def compute_grades(self):
        grades = {}
        for course, score in self.courses.items():
            if score >= 70 and score <= 100:
                grades[course] = "A"
            elif score >= 60 and score <= 69:
                grades[course] = "B"
            elif score >= 50 and score <= 59:
                grades[course] = "C"
            elif score >= 45 and score <= 49:
                grades[course] = "D"
            elif score >= 40 and score <= 44:
                grades[course] = "E"
            else:
                grades[course] = "F"
        return grades

    def compute_points(self):
        points = {}
        for course, score in self.courses.items():
            if score >= 70 and score <= 100:
                points[course] = 5
            elif score >= 60 and score <= 69:
                points[course] = 4
            elif score >= 50 and score <= 59:
                points[course] = 3
            elif score >= 45 and score <= 49:
                points[course] = 2
            elif score >= 40 and score <= 44:
                points[course] = 1
            else:
                points[course] = 0
        return points

    def compute_remarks(self):
        remarks = {}
        for course, score in self.courses.items():
            if score >= 70 and score <= 100:
                remarks[course] = "Excellent"
            elif score >= 60 and score <= 69:
                remarks[course] = "Very Good"
            elif score >= 50 and score <= 59:
                remarks[course] = "Good"
            elif score >= 45 and score <= 49:
                remarks[course] = "Satisfactory"
            elif score >= 40 and score <= 44:
                remarks[course] = "Adequate"
            else:
                remarks[course] = "Failure"
        return remarks

  
    def print_grades(self):
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")

    def print_points(self):
        for course, point in self.points.items():
            print(f"{course}: {point}")

    def print_remarks(self):
        for course, remark in self.remarks.items():
            print(f"{course}: {remark}")


student = Student(
    "John Doe",
    20,
    {
        "math": 85,
        "physics": 75,
        "chemistry": 95,
        "biology": 65,
        "english": 80,
        "history": 70,
        "geography": 60,
        "cre": 55,
        "agriculture": 45,
        "french": 40,
        "kiswahili": 35,
    },
)
student.print_grades()
student.print_points()
student.print_remarks()
