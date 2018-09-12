class Person:
    def __init__(self,name,profecion,salary):
        self.personal_date=(name,profecion,salary)
    def __str__(self):
        return "Name:  %s,  Profeccion: %s,  Salary : %s)" % self.personal_date
class Manager(Person):
    def __init__(self,name):
       self.personal_date=(name,'Manager',15000.50)

manager1=Manager("Oksana")
person1=Person("Ivan","driwer",10000.35)
print(manager1)
print(person1)