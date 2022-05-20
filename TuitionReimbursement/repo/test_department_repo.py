import unittest

from models.department import Department
from repo.department_repo_impl import DepartmentRepoImpl

dr = DepartmentRepoImpl()


class TestDepartmentRepo(unittest.TestCase):
    added_department = Department()

    def test_1_get_department_success(self):
        department = dr.get_department(1)
        self.assertEqual(department, Department(d_id=1, dep_head=1, dep_name="Business"))

    def test_2_create_department_success(self):
        TestDepartmentRepo.added_department = dr.create_department(self.added_department)

        self.assertEqual(self.added_department, Department(d_id=self.added_department.d_id, dep_head=0,
                                                           dep_name=''))

        self.assertIsNotNone(dr.get_department(self.added_department.d_id))
        print(self.added_department)

    def test_3_update_department_success(self):
        TestDepartmentRepo.added_department = dr.update_department(Department(d_id=self.added_department.d_id,
                                                                              dep_head=0, dep_name='science'))

        self.assertEqual(self.added_department.dep_name, "science")

    def test_4_delete_department_success(self):
        self.assertIsNotNone(dr.delete_department(self.added_department.d_id))


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
