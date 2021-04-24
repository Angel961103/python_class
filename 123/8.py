from typing import MappingView

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Angel", 13)
print(s.name)
print(s.age)
s2 = Student("Evelyn", 14)
print(s2.name)
print(s2.age)