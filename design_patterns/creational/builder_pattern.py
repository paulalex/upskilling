from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    """ 
    Define an abstract base class for builders that should all have a build method
    """
    @abstractmethod
    def build(self) -> None:
        pass


class ProductABuilder(Builder):
    _product_a = None

    def __init__(self) -> None:
        print("[INFO] Building Product A")
        self._product_a = ProductA()

    def with_property_a(self, property_a):
        print("[INFO] Setting Property A")
        self._product_a.set_property_a(property_a)

        return self

    def with_property_b(self, property_b):
        print("[INFO] Setting Property B")
        self._product_a.set_property_b(property_b)

        return self

    def build(self) -> ProductA:
        print("[INFO] Building complex object product A")
        print(self)
        return self._product_a

    def __repr__(self):
        return f"[INFO] product_a=[property_a={self._product_a.get_property_a()}, " \
               f"property_b={self._product_a.get_property_b()}]"


class ProductA:
    _propertyA = None
    _propertyB = None

    def __init__(self) -> None:
        print("[INFO] Initialising Product Object")

    def set_property_a(self, property_a) -> None:
        self._propertyA = property_a

    def set_property_b(self, property_b) -> None:
        self._propertyB = property_b

    def get_property_a(self) -> None:
        return self._propertyA

    def get_property_b(self) -> None:
        return self._propertyB

def example_client_code(product_a_builder):
    product_a = product_a_builder\
        .with_property_a("Property A")\
        .with_property_b("Property B")\
        .build()

    return product_a


if __name__ == "__main__":
    print("Builder pattern demo")

    product_a = ProductABuilder()\
        .with_property_a("Property A")\
        .with_property_b("Property B")\
        .build()
