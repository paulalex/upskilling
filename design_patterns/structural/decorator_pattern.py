from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def get_employee_number(self) -> str:
        pass

    @abstractmethod
    def get_employee_number_prefix(self) -> str:
        pass

class FulltimeEmployee(Employee):
    _employee_number = None

    def __init__(self, employee_number):
        super().__init__()
        self._employee_number = employee_number

    def get_employee_number(self) -> str:
        return self._employee_number

    def get_employee_number_prefix(self) -> str:
        return f"PERM"

def print_employee_number(employee):
    print(f"{employee.get_employee_number_prefix()}-{employee.get_employee_number()}\n")

class ContractorEmployeeDecorator(Employee):
    _employee = None

    def set_employee(self, employee) -> None:
        self._employee = employee

    def get_employee_number(self) -> str:
        return f"0000{self._employee.get_employee_number()}"

    def get_employee_number_prefix(self) -> str:
        return f"CONTRACT-{self._employee.get_employee_number_prefix()}"

if __name__ == "__main__":
    
    employee = FulltimeEmployee("123456")

    contractor = ContractorEmployeeDecorator()
    contractor.set_employee(FulltimeEmployee("11111111"))

    print("[INFO] Standard Employee")
    print_employee_number(employee)

    print("[INFO] Contractor Employee needs to have their employee number and employee number prefix modified")
    print_employee_number(contractor)