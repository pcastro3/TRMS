from abc import ABC, abstractmethod


class EventRepo(ABC):

    @abstractmethod
    def get_event(self, ev_id):
        pass


