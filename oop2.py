class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
   
    def movement(self):
        print("Person is walking")
    def myfunc(self):
        print("Hello my name is " + self.name + "I am " + str(self.age) + "years old, " + self.gender + " is my gender")
p1 = person("John", 36, "Male")
p2 = person("Mary", 34, "Female")
p3 = person("Josh", 29, "Male")
p1.myfunc()
p2.myfunc()
p3.myfunc()
p1.movement()
p2.movement()
p3.movement()