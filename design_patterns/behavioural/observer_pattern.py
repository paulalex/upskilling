from __future__ import annotations
from abc import ABC, abstractmethod

class Observable(ABC):
    _observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.notify()

class Observer(ABC):
    @abstractmethod
    def notify(self):
        pass

class DataStorage(Observable):
    def save_data(self, data):
        print(f"Persisted Data {data}")
        self.notify_observers()

class EmailNotification(Observer):
    def notify(self):
        print("Email notifier is sending an email when record was saved")

class SMSNotification(Observer):
    def notify(self):
        print("SMS notifier is sending a text message when record was saved")

class GUI(Observer):
    def notify(self):
        print("GUI is alerting user that record saved successfully")

if __name__ == "__main__":
    database = DataStorage()
    components = [GUI(), EmailNotification(), SMSNotification()]
    
    for component in components:
        database.add_observer(component)

    data = "{name: John, age: 25}"

    print("[INFO] Saving data", end="\n\n")
    database.save_data(data)
