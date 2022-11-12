class Person:
    def __init__(self,name):
        self.name = name
    
class Dog:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

ken = Person('けん')
pochi = Dog('ぽち',ken)

print(pochi.owner.name)