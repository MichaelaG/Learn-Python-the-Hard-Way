# Example 42

## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal is-a object
class Dog(Animal):
    def __init__(self, name):
        ## dog has-a name
        self.name = name

## Cat is-a Animal is-a object
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None

## Employee is-a Person is-a object
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has-a super function that initializes the name parameter
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish is-a object
class Salmon(Fish):
    pass

# Halibut is-a Fish is-a object
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
