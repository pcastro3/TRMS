import unittest

from models.employee import Employee
from repo.employee_repo_impl import EmployeeRepoImpl

er = EmployeeRepoImpl()


class TestEmployeeRepo(unittest.TestCase):
    added_employee = Employee()

    def test_1_get_employee_success(self):
        employee = er.get_employee(1)
        self.assertEqual(employee, Employee(emp_id=1, full_name='joel miller', email='joel@mail.com',
                                            password='password', superv_id=2, dep_id=1))

    def test_2_create_employee_success(self):
        TestEmployeeRepo.added_employee = er.create_employee(self.added_employee)

        self.assertEqual(self.added_employee, Employee(emp_id=self.added_employee.emp_id, full_name='',
                                                       email='', password='', superv_id=0, dep_id=0))

        self.assertIsNotNone(er.get_employee(self.added_employee.emp_id))
        print(self.added_employee)

    def test_3_update_employee_success(self):
        TestEmployeeRepo.added_employee = er.update_employee(Employee(emp_id=self.added_employee.emp_id,
                                                                      full_name='new', email='', password='',
                                                                      superv_id=0, dep_id=0))

        self.assertEqual(self.added_employee.full_name, "new")
        print(self.added_employee)

    def test_4_delete_employee_success(self):
        self.assertIsNotNone(er.delete_employee(self.added_employee.emp_id))


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
