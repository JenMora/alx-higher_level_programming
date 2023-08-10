class Jeniffer:
"""This is a module that describes a person"""


    def __init__(self, name, age, sign, likes, school):
        self.name = name
        self.age = age
        self.sign = sign
        self.likes = likes
        self.school = school

me = Jeniffer("Jen Doe", 22, "Gem", "codes", "Alx")
print(me.name)
print(me.age)
print(me.sign)
print(me.likes)
print(me.school)
