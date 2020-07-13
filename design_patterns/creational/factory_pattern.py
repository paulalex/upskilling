from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def pour(self):
        pass

class Coke(Drink):
    def pour(self):
        print(f"Pouring Coke.....")

class Pepsi(Drink):
    def pour(self):
        print(f"Pouring Pepsi.....")

class Sprite(Drink):
    def pour(self):
        print(f"Pouring Sprite.....")

class Lilt(Drink):
    def pour(self):
        print(f"Pouring Lilt.....")

class DrinkFactory(ABC):
    def create(self):
        return Coke()

class CokeFactory(DrinkFactory):
    def create(self):
        return Coke()

class PepsiFactory(DrinkFactory):
    def create(self):
        return Pepsi()

class SpriteFactory(DrinkFactory):
    def create(self):
        return Sprite()

class LiltFactory(DrinkFactory):
    def create(self):
        return Lilt()


if __name__ == "__main__":
    factories = [CokeFactory(), PepsiFactory(), SpriteFactory(), LiltFactory()]

    for factory in factories:
        factory.create().pour()