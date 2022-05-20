from repo.employee_repo import EmployeeRepo
from repo.employee_repo_impl import EmployeeRepoImpl


class EmployeeService:

    def __init__(self, employee_repo: EmployeeRepo):
        self.employee_repo = employee_repo

    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)

    def get_employee_by_id(self, emp_id):
        return self.employee_repo.get_employee(emp_id)

    def get_all_employees(self):
        return self.employee_repo.all_employees()

    def get_employee_by_dep(self, dep_id, emp_id):
        return self.employee_repo.get_employee_by_dep(dep_id, emp_id)

    def get_all_employees_by_dep(self, dep_id):
        return self.employee_repo.get_all_employees_by_dep(dep_id)

    def update_employee(self, change):
        return self.employee_repo.update_employee(change)

    def delete_employee(self, emp_id):
        return self.employee_repo.delete_employee(emp_id)


def _test():
    pass


if __name__ == '__main__':
    _test()
