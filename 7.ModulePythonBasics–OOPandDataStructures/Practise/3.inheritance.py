class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

p1 = Person("Soykot",27)

print(p1.Name)

class NewPerson(Person):
    def __init__(self, name, age,color,adress):
        super().__init__(name, age)

        self.Color = color
        self.Address = adress
        self.Name = name+" Chowdhury"

newperson = NewPerson("Utshab",26,"White","Dhaka")

print(newperson.Name)



