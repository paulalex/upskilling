from abc import ABC, abstractmethod

class AbstractHandler(ABC):
    """Defines a contract for all AWS lambda handlers that follow the CRUD convention.

    Define functions to:
        Create
        Read
        Update
        Delete
        Read All Records
    """
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