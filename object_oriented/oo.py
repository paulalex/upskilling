from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def breathe(self) -> None:
        pass

class Mammal(Animal):
    @abstractmethod
    def speak(self) -> None:
        pass
    
    def breathe(self) -> None:
        """Override the breathe method by defining a new implementation for it
        """
        print("Breathes oxygen")

class Omnivore(Mammal):
    def eat(self) -> None:
        print("Eats meat and plants")

class Carnivore(Mammal):
    def eat(self) -> None:
        print("Eats meat only")

class Herbivore(Mammal):
    def eat(self) -> None:
        print("Eats plants only")

class Human(Omnivore):
    _name = None
    _eye_colour = None
    _hair_colour = None
    _build = None

    def __init__(self, name: str, eye_colour: str, hair_colour: str, build: str) -> None:
        super().__init__()
        self._name = name
        self._eye_colour = eye_colour
        self._hair_colour = hair_colour
        self._build = build

    def speak(self) -> None:
        print(f"Hello my name is {self._name}")
    
    def breathe(self) -> None:
        print("Breathes oxygen but uses an asthma inhaler")

    def eat(self) -> None:
        print("Eats burgers")

    def get_attributes(self) -> tuple:
        """Get the attributes of this Human, this is a method specific to this object type

        Returns:
            name (str): The persons name
            eye_colour (str): The persons eye colour
            hair_colour (str): The person hair colour
            build (str): The persons build
        """
        return (self._name, self._eye_colour, self._hair_colour, self._build)

class Dog(Carnivore):
    def speak(self) -> None:
        print("Barks")

class Cow(Herbivore):
    _bell = None

    def __init__(self, bell: str) -> None:
        """Constructor serves as the mechanism for creating your objects, python does not support multiple constructorsS
        Args: 
            bell (str): The type of bell that this cow wears
        """
        super().__init__()
        self._bell = bell

    def speak(self) -> None:
        print("Moos")

    def get_bell(self) -> str:
        return self._bell

if __name__ == "__main__":
    print("[INFO] Object Oriented Concepts Demo", end="\n\n")

    print("[INFO] Human")
    john = Human("John", "Black", "Green", "Medium")
    john.eat()
    john.breathe()
    john.speak()
    print(f"Human Attributes: {john.get_attributes()}")
    print("\n")

    print("[INFO] Dog")
    dog = Dog()
    dog.eat()
    dog.breathe()
    dog.speak()
    print("\n")

    print("[INFO] Cow")
    cow = Cow("Cowbell")
    cow.eat()
    cow.breathe()
    cow.speak()
    print(cow.get_bell())
    print("\n")

    print("[INFO] Polymorphism - means an object can have many forms (it can be more than one thing...)")
    print(f"Cow is an animal: {isinstance(cow, Animal)}")
    print(f"Cow is a mammal: {isinstance(cow, Mammal)}")
    print(f"Cow is a herbivore: {isinstance(cow, Herbivore)}")
    print(f"Cow is a cow: {isinstance(cow, Cow)}")
    print(f"Cow is a dog: {isinstance(cow, Dog)}")
    print("\n")

    print("[INFO] In many OO languages an abstract class CANNOT be instantiated")
    try:
        animal = Animal()
    except Exception as e:
        print(e)
    print("\n")

    print("[INFO] We can type cast an object to 'force' it into some other type that is in its inheritance tree")
    john.breathe()
    john.__class__ = Mammal
    john.breathe()
    print("\n")

    print("[INFO] Its worth noting that python doesnt support method Overloading")
    def add(a, b):
        return a + b

    def add(a, b, c):
        return a + b + c

    print(add(1, 2, 3), end="\n\n")

    try:
        print("[INFO] The following function, instead of calling the version which accepts two parameters, calling below with two arguments results in an error", end="\n\n")
        print(add(1, 2))
    except Exception as e:
        print(e, end="\n\n")