# This class was applied for inheritance
# and polymorphism and abstraction , encapsulation

class Animal(object):
    def __init__(self, name):
        self.name = name
    def speak(self):
        """Abtraction method"""
        raise NotImplementedError
    def walk(self):
        """Abtraction method"""
        raise NotImplementedError
class Dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print('gau gau gau ')
        self.__eat()

    def increase_or_not(self,time):
        if time > 2:
            self.__increase_age()

    def __eat(self):
        print("I'm eating")

    def __increase_age(self):
        self.age +=1

class Cat(Animal):
    def speak(self):
        print('meo meo meo')


mycat =Cat('titi')
mydog = Dog('mimi', 14)

mycat.speak()
mydog.speak()
#mydog.walk()
#mydog.__eat()"









