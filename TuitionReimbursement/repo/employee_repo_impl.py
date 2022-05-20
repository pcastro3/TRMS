from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repo.employee_repo import EmployeeRepo
from util.db_connection import connection


def _build_employee(record):
    if record:
        return Employee(emp_id=record[0], full_name=record[1], email=record[2], password=record[3],
                        superv_id=record[4], dep_id=record[5])
    else:
        return None


class EmployeeRepoImpl(EmployeeRepo):

    def create_employee(self, employee):
        sql = "INSERT INTO employees VALUES (DEFAULT, %s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [employee.full_name, employee.email, employee.password,
                             employee.superv_id, employee.dep_id])
        connection.commit()
        record = cursor.fetchone()
        return _build_employee(record)

    def get_employee(self, emp_id):
        sql = "SELECT * FROM employees WHERE emp_id=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [emp_id])

        record = cursor.fetchone()

        if record:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with id: {emp_id} - Not Found")

    def all_employees(self):
        sql = "SELECT * FROM employees"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        # if records:
        account_list = [_build_employee(record) for record in records]
        return account_list
        # else:
        #     raise ResourceNotFound(f"No Employees")

    def get_employee_by_dep(self, dep_id, emp_id):
        sql = "SELECT * FROM employees WHERE emp_id=%s AND dep_id=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [dep_id, emp_id])

        record = cursor.fetchone()

        if record:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with id: {emp_id} - Not Found")

    def get_all_employees_by_dep(self, dep_id):
        sql = "SELECT * FROM employees WHERE dep_id=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [dep_id])

        records = cursor.fetchall()

        if records:
            employee_list = [_build_employee(record) for record in records]
            return employee_list
        else:
            raise ResourceNotFound(f"There are no Employees")

    def update_employee(self, change):
        sql = "UPDATE employees SET full_name=%s, email=%s, password=%s, superv_id=%s, dep_id=%s" \
              " WHERE emp_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.full_name, change.email, change.password,
                             change.superv_id, change.dep_id, change.emp_id])
        connection.commit()
        record = cursor.fetchone()

        if record:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with id: {change.emp_id} - Not Found")

    def delete_employee(self, emp_id):
        sql = "DELETE FROM employees WHERE emp_id = %s RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [emp_id])

        connection.commit()
        record = cursor.fetchone()

        if record:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Department with id: {emp_id} - Not Found")


def _test():
    pass


if __name__ == '__main__':
    _test()
