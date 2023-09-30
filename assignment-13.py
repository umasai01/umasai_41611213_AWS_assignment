class Animal:
    def __init__(self, name): # Single inheritance
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says bow!"

my_dog = Dog("snowie")
print(my_dog.speak())  


class Flyable:    # Multilevel inheritance
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class Bird(Flyable, Swimmer):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} koo koo!"

Bird = Bird("Robin")
print(Bird.speak())  
Bird.fly()           
Bird.swim()       



class Vehicle:
    def __init__(self, name):   # Hierarchical Inheritance
        self.name = name

   
class Car(Vehicle):
    def model(self):
        return f"{self.name} car"

class Bike(Vehicle):
    def model(self):
        return f"{self.name} motor cycle"

my_car = Car("Toyota")
my_bike = Bike("Honda")
print(my_car.model())  
print(my_bike.model())  
