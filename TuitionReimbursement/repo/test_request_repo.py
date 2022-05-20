import unittest

from models.request import Request
from repo.request_repo_impl import RequestRepoImpl

er = RequestRepoImpl()


class TestRequestRepo(unittest.TestCase):
    added_request = Request()

    def test_1_get_request_success(self):
        request = er.get_request(3, 2)
        self.assertEqual(request, Request(req_id=2, cost=250, grade='B', event_date=1, location='S St',
                                          event_id=4, employee_id=3, status='tuition reimbursement approved'))

    def test_2_create_request_success(self):
        TestRequestRepo.added_request = er.create_request(self.added_request)

        self.assertEqual(self.added_request, Request(req_id=0, cost=0, grade='', event_date=0, location='',
                                                     event_id=0, employee_id=0, status=''))

        self.assertIsNotNone(er.get_request(self.added_request.req_id))
        print(self.added_request)

    def test_3_update_request_success(self):
        TestRequestRepo.added_request = er.update_request(Request(req_id=self.added_request.req_id, cost=0,
                                                                  grade='', event_date=0, location='new',
                                                                  event_id=0, employee_id=0, status=''))

        self.assertEqual(self.added_request.location, "new")
        print(self.added_request)

    def test_4_delete_request_success(self):
        self.assertIsNotNone(er.delete_request(self.added_request.employee_id, self.added_request.req_id))


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
