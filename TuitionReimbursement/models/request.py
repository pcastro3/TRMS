class Request:

    def __init__(self, req_id=0, cost=0, grade='', event_date=0, location='',
                 event_id=0, employee_id=0, status=''):
        self.req_id = req_id
        self.cost = cost
        self.grade = grade
        self.event_date = event_date
        self.location = location
        self.event_id = event_id
        self.employee_id = employee_id
        self.status = status

    def __repr__(self):
        return str({
            'req_id': self.req_id,
            'cost': self.cost,
            'grade': self.grade,
            'event_date': self.event_date,
            'location': self.location,
            'event_id': self.event_id,
            'employee_id': self.employee_id,
            'status': self.status,
        })

    def json(self):
        return {
            'reqId': self.req_id,
            'cost': self.cost,
            'grade': self.grade,
            'eventDate': self.event_date,
            'location': self.location,
            'eventId': self.event_id,
            'employeeId': self.employee_id,
            'status': self.status,
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Request):
            return False

        return self.__dict__ == other.__dict__
