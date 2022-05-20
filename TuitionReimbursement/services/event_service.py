from repo.event_repo import EventRepo
from exceptions.resource_unavailable import ResourceUnavailable
from models.event import Event
from repo.event_repo_impl import EventRepoImpl


class EventService:

    def __init__(self, event_repo: EventRepo):
        self.event_repo = event_repo

    def get_event_by_id(self, ev_id):
        return self.event_repo.get_event(ev_id)


def _test():
    pass


if __name__ == '__main__':
    _test()
