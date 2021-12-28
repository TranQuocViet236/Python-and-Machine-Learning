from abc import  ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating!")

class Fish(Animal):
    def eat(self):
        print("This fish is eating!")


if __name__ == "__main__":
    rabbit = Rabbit()
    fish = Fish()
    rabbit.eat()
    fish.eat()