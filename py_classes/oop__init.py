class Person:
     def __init__(self, name):
         self.name = name
     def say_hi(self):
         print('Hello you, my name is',self.name)
p = Person('jen')
p.say_hi()
