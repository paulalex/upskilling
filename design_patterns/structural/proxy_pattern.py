from abc import ABC, abstractmethod

class ExpensiveObject(ABC):
    @abstractmethod
    def expensive_call(self) -> None:
        pass

class ExpensiveObjectImpl(ExpensiveObject):
    def __init__(self):
        super().__init__()
        self._configure()

    def expensive_call(self) -> None:
        print("Processing is complete")

    def _configure(self):
        for i in range(1, 1000):
            print("Long running configuration call like a connection set up")

class ExpensiveObjectProxy(ExpensiveObject):
    _expensive_object = None

    def expensive_call(self) -> str:
        if not self._expensive_object:
            self._expensive_object = ExpensiveObjectImpl()
            self._expensive_object.expensive_call()
        else:
            self._expensive_object.expensive_call()

if __name__ == "__main__":
    proxy = ExpensiveObjectProxy()

    proxy.expensive_call()
    proxy.expensive_call()
    proxy.expensive_call()

