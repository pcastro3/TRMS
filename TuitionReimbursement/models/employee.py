class Employee:

    def __init__(self, emp_id=0, full_name='', email='', password='',
                 superv_id=0, dep_id=0):
        self.emp_id = emp_id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.superv_id = superv_id
        self.dep_id = dep_id

    def __repr__(self):
        return str({
            'emp_id': self.emp_id,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'superv_id': self.superv_id,
            'dep_id': self.dep_id
        })

    def json(self):
        return {
            'empId': self.emp_id,
            'fullName': self.full_name,
            'email': self.email,
            'password': self.password,
            'supervId': self.superv_id,
            'depId': self.dep_id
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Employee):
            return False

        return self.__dict__ == other.__dict__


def _test():
    employee1 = Employee()
    employee2 = Employee()

    print(employee1 == employee2)

    employee1 = Employee(full_name="new")
    employee2 = Employee(full_name="new")

    print(employee1 == employee2)


if __name__ == '__main__':
    _test()
