#Parent class
class Animal:
    def speak(self):
        print("Animal is speaking")
#Child class
class Dog:
    def bark(self):
        print("Dog is barking")

a = Animal()
a.speak()
d = Dog()
d.bark()