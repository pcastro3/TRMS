from repo.request_repo import RequestRepo
from exceptions.resource_unavailable import ResourceUnavailable
from models.request import Request
from repo.request_repo_impl import RequestRepoImpl


class RequestService:

    def __init__(self, request_repo: RequestRepo):
        self.request_repo = request_repo

    def create_request(self, req):
        return self.request_repo.create_request(req)

    def get_request_by_id(self, employee_id, req_id):
        return self.request_repo.get_request(employee_id, req_id)

    def get_all_requests(self, employee_id):
        return self.request_repo.all_requests(employee_id)

    def update_request(self, change):
        return self.request_repo.update_request(change)

    def update_status(self, change):
        return self.request_repo.update_status(change)

    def delete_request(self, employee_id, req_id):
        return self.request_repo.delete_request(employee_id, req_id)

    def approve_request(self, employee_id, req_id):
        requests = self.get_request_by_id(employee_id, req_id)

        if requests.status == 'pending supervisor':
            requests.status = 'pending department head'
            self.update_request(requests)
            return requests
        elif requests.status == 'pending department head':
            requests.status = 'pending benefits coordinator'
            self.update_request(requests)
            return requests
        elif requests.status == 'pending benefits coordinator':
            requests.status = 'tuition reimbursement approved'
            self.update_request(requests)
            return requests
        else:
            ResourceUnavailable(f"No status yet.")


def _test():
    pass


if __name__ == '__main__':
    _test()
