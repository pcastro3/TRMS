from abc import ABC, abstractmethod


class RequestRepo(ABC):

    @abstractmethod
    def create_request(self, req):
        pass

    @abstractmethod
    def get_request(self, employee_id, req_id):
        pass

    @abstractmethod
    def all_requests(self, employee_id):
        pass

    @abstractmethod
    def update_request(self, change):
        pass

    @abstractmethod
    def update_status(self, change):
        pass

    @abstractmethod
    def delete_request(self, employee_id, req_id):
        pass

