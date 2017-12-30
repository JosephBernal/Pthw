## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a class
class Cat(Animal):

    def __init__(self,name):
        ## Cat has-a name
        self.name = name

## Person is-an object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

    ## Person has-a pet of some kind
    self.pet = None

## Employee is-a class
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name, salary hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is a sub-class of fish
class Salmon(Fish):
    pass

## Halibut is also a sub-class of fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has a pet named satan
mary.pet = satan

## frank is an employee who makes 120k
frank = Employee("Frank", 120000)

## frank has a pet named rover
frank.pet = rover

## Flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()