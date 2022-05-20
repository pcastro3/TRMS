class Department:

    def __init__(self, d_id=0, dep_head=0, dep_name=''):
        self.d_id = d_id
        self.dep_head = dep_head
        self.dep_name = dep_name

    def __repr__(self):
        return str({
            'd_id': self.d_id,
            'dep_head': self.dep_head,
            'dep_name': self.dep_name
        })

    def json(self):
        return {
            'dId': self.d_id,
            'depHead': self.dep_head,
            'depName': self.dep_name
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Department):
            return False

        return self.__dict__ == other.__dict__


def _test():
    department1 = Department()
    department2 = Department()

    print(department1 == department2)

    department1 = Department(dep_name="Business")
    department2 = Department(dep_name="Business")

    print(department1 == department2)


if __name__ == '__main__':
    _test()
