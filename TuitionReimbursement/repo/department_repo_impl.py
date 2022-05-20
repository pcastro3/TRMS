from exceptions.resource_not_found import ResourceNotFound
from models.department import Department
from repo.department_repo import DepartmentRepo
from util.db_connection import connection


def _build_department(record):
    if record:
        return Department(d_id=record[0], dep_head=record[1], dep_name=record[2])
    else:
        return None


class DepartmentRepoImpl(DepartmentRepo):

    def create_department(self, department):
        sql = "INSERT INTO department VALUES (DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [department.dep_head, department.dep_name])

        connection.commit()
        record = cursor.fetchone()
        return _build_department(record)

    def get_department(self, d_id):
        sql = "SELECT * FROM department WHERE d_id=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [d_id])

        record = cursor.fetchone()

        if record:
            return _build_department(record)
        else:
            raise ResourceNotFound(f"Department with id: {d_id} - Not Found")

    def all_departments(self):
        sql = "SELECT * FROM department"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        if records:
            department_list = [_build_department(record) for record in records]
            return department_list
        else:
            raise ResourceNotFound(f"No departments")

    def update_department(self, change):
        sql = "UPDATE department SET dep_head=%s, dep_name=%s" \
              " WHERE d_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.dep_head, change.dep_name, change.d_id])

        connection.commit()
        record = cursor.fetchone()

        if record:
            return _build_department(record)
        else:
            raise ResourceNotFound(f"Department with id: {change.d_id} - Not Found")

    def delete_department(self, d_id):
        sql = "DELETE FROM department WHERE d_id = %s RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [d_id])

        connection.commit()
        record = cursor.fetchone()

        if record:
            return _build_department(record)
        else:
            raise ResourceNotFound(f"Department with id: {d_id} - Not Found")


def _test():
    pass


if __name__ == '__main__':
    _test()


