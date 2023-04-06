#A Class is the blueprint of what an item could be.
class Person:
    #class level attributes
    
    # initializer / constructor 
    #self is used in Python, other lang may use -- "this"
    def __init__(self, name, age, eyecolor):
        self.name = name
        self.age = age
        self.eyecolor = eyecolor


#Outside the class 
#Object Below
Scott = Person('Scott',43,'blue') #Scott is an instance of the Person class
jill = Person('Jill',35,'green') #Jill is an instance of the Person class

#attributes can be assigned to an object using the . operator

print(Scott.name, "age is", Scott.age, "eye color is", Scott.eyecolor)

jill.age = 35

print("Jill's age is", jill.age)

print(Scott)