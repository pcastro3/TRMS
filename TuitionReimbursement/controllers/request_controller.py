from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.request import Request
from repo.request_repo_impl import RequestRepoImpl
from services.request_service import RequestService

rr = RequestRepoImpl()
rs = RequestService(rr)


def route(app):
    @app.route("/employee/<employee_id>/request", methods=["GET"])
    def get_all_requests(employee_id):
        try:
            return jsonify([req.json() for req in rs.get_all_requests(employee_id)]), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employee_id>/request/<req_id>", methods=["GET"])
    def get_request(employee_id, req_id):
        try:
            return rs.get_request_by_id(employee_id, req_id).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employee_id>/request", methods=["POST"])
    def post_request(employee_id):
        body = request.json
        print(body)
        print("here")
        req = Request(employee_id=employee_id, event_id=body["eventId"], cost=body["cost"],
                      grade=body["grade"], event_date=body["eventDate"], location=body["location"])
        print("here1")
        req = rs.create_request(req)
        print("here2")
        print(req)
        return req.json(), 201

    @app.route("/employee/<employee_id>/request/<req_id>", methods=["PUT"])
    def update_request(employee_id, req_id):
        try:
            body = request.json
            print("here")
            req = Request(employee_id=employee_id, req_id=req_id, cost=body["cost"],
                          event_date=body["eventDate"], location=body["location"], status=body["status"])
            print("here1")
            req = rs.update_request(req)
            return req.json(), 204

        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employee_id>/request/<req_id>", methods=["PATCH"])
    def approve_request(employee_id, req_id):
        action = request.json['action']
        if action == "approve":
            try:
                req = rs.approve_request(employee_id, req_id)
                # body = request.json
                # req = Request(employee_id=employee_id, req_id=req_id, status=body["status"])

                # req = rs.approve_request(employee_id, req_id)
                return f"Successfully Updated Status For Employee with ID: {req.employee_id}", 204

            except ValueError as e:
                return "Not a valid ID", 400
            except ResourceNotFound as r:
                return r.message, 404

    @app.route("/employee/<employee_id>/request/<req_id>", methods=["DELETE"])
    def del_request(employee_id, req_id):
        try:
            rs.delete_request(employee_id, req_id)
            return '', 204
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404


def _test():
    pass


if __name__ == '__main__':
    _test()
