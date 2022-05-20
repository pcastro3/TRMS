from abc import ABC, abstractmethod


class EmployeeRepo(ABC):

    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def get_employee(self, emp_id):
        pass

    @abstractmethod
    def all_employees(self):
        pass

    @abstractmethod
    def get_employee_by_dep(self, dep_id, emp_id):
        pass

    @abstractmethod
    def get_all_employees_by_dep(self, dep_id):
        pass

    @abstractmethod
    def update_employee(self, change):
        pass

    @abstractmethod
    def delete_employee(self, emp_id):
        pass

