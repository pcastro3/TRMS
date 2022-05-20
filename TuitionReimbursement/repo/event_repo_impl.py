from exceptions.resource_not_found import ResourceNotFound
from models.event import Event
from repo.event_repo import EventRepo
from util.db_connection import connection


def _build_event(record):
    return Event(ev_id=record[0], event_type=record[1], percentage=record[2])


class EventRepoImpl(EventRepo):

    def get_event(self, ev_id):
        sql = "SELECT * FROM events WHERE ev_id=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [ev_id])

        record = cursor.fetchone()

        if record:
            return _build_event(record)
        else:
            raise ResourceNotFound(f"Event with id: {ev_id} - Not Found")


def _test():
    pass


if __name__ == '__main__':
    _test()
