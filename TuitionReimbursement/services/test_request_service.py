import unittest
from unittest.mock import MagicMock

from models.request import Request
from repo.request_repo_impl import RequestRepoImpl
from services.request_service import RequestService


class TestRequestService(unittest.TestCase):
    rr = RequestRepoImpl()
    rs = RequestService(rr)

    def test_get_request_by_id(self):
        self.rs.get_request_by_id = MagicMock(return_value=[
            Request(req_id=1, cost=770, grade='B', event_date=1, location='new st',
                    event_id=4, employee_id=2)
        ])

        refined_requests = self.rs.approve_request(2, 1)
        print(refined_requests)

        self.assertListEqual(refined_requests, [
            Request(req_id=1, cost=770, grade='B', event_date=1, location='new st',
                    event_id=4, employee_id=2, status='pending supervisor')
        ])


if __name__ == '__main__':
    unittest.main()
