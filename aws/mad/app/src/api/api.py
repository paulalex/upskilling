from abc import ABC, abstractmethod

class AbstractHandler(ABC):
    @abstractmethod
    def create_handler(self, event, context):
        pass

    @abstractmethod
    def read_handler(self, event, context):
        pass

    @abstractmethod
    def read_all_handler(self, event, context):
        pass

    @abstractmethod
    def update_handler(self, event, context):
        pass

    @abstractmethod
    def delete_handler(self, event, context):
        pass