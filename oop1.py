class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        print(self.name, "has a grade of", self.grade)

student1 = student("John", 15, "A")
student1.get_grade()

student2 = student("Mary", 16, "B")
student2.get_grade()