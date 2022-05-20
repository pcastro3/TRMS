from models.department import Department
from repo.department_repo import DepartmentRepo


class DepartmentService:

    def __init__(self, department_repo: DepartmentRepo):
        self.department_repo = department_repo

    def create_department(self, department):
        return self.department_repo.create_department(department)

    def get_department_by_id(self, d_id):
        return self.department_repo.get_department(d_id)

    def get_all_departments(self):
        return self.department_repo.all_departments()

    def update_department(self, change):
        return self.department_repo.update_department(change)

    def delete_department(self, d_id):
        return self.department_repo.delete_department(d_id)


def _test():
    pass


if __name__ == '__main__':
    _test()
