from abc import ABC, abstractmethod


class DepartmentRepo(ABC):

    @abstractmethod
    def create_department(self, department):
        pass

    @abstractmethod
    def get_department(self, d_id):
        pass

    @abstractmethod
    def all_departments(self):
        pass

    @abstractmethod
    def update_department(self, change):
        pass

    @abstractmethod
    def delete_department(self, d_id):
        pass

