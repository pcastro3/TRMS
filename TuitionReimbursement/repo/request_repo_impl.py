from exceptions.resource_not_found import ResourceNotFound
from models.request import Request
from repo.request_repo import RequestRepo
from util.db_connection import connection


def _build_request(record):
    return Request(req_id=record[0], cost=float(record[1]), grade=record[2],
                   event_date=record[3], location=record[4], event_id=record[5],
                   employee_id=record[6], status=record[7])


class RequestRepoImpl(RequestRepo):

    def create_request(self, req):
        sql = "INSERT INTO requests VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, DEFAULT) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [req.cost, req.grade, req.event_date,
                             req.location, req.event_id, req.employee_id])

        connection.commit()
        record = cursor.fetchone()
        return _build_request(record)

    def get_request(self, employee_id, req_id):
        sql = "SELECT * FROM requests WHERE employee_id=%s AND req_id=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [employee_id, req_id])

        record = cursor.fetchone()

        if record:
            return _build_request(record)
        else:
            raise ResourceNotFound(f"Request with id: {req_id} - Not Found")

    def all_requests(self, employee_id):
        sql = "SELECT * FROM requests WHERE employee_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        records = cursor.fetchall()

        if records:
            request_list = [_build_request(record) for record in records]
            return request_list
        else:
            raise ResourceNotFound(f"No requests for employee {employee_id}.")

    def update_request(self, change):
        print(change)
        sql = "UPDATE requests SET cost=%s, event_date=%s," \
              " location=%s, status=%s WHERE req_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.cost, change.event_date,
                             change.location, change.status, change.req_id])

        connection.commit()
        record = cursor.fetchone()

        if record:
            return _build_request(record)
        else:
            raise ResourceNotFound(f"Request with id: {change.req_id} - Not Found")

    def update_status(self, change):
        sql = "UPDATE requests SET status=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.status])

        connection.commit()
        record = cursor.fetchone()

        if record:
            return _build_request(record)
        else:
            raise ResourceNotFound(f"Request with id: {change.req_id} - Not Found")

    def delete_request(self, employee_id, req_id):
        sql = "DELETE FROM requests WHERE employee_id=%s AND req_id=%s"

        if req_id:
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id, req_id])
            connection.commit()
        else:
            raise ResourceNotFound(f"Request with id: {req_id} - Not Found")


def _test():
    pass


if __name__ == '__main__':
    _test()
