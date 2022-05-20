from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repo.employee_repo_impl import EmployeeRepoImpl
from services.employee_service import EmployeeService

er = EmployeeRepoImpl()
es = EmployeeService(er)


def route(app):
    @app.route("/employee", methods=["GET"])
    def get_all_employees():
        return jsonify([employee.json() for employee in es.get_all_employees()])

    @app.route("/employee/<emp_id>", methods=["GET"])
    def get_employee(emp_id):
        try:
            print("here")
            return es.get_employee_by_id(int(emp_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department/<dep_id>/employee/<emp_id>", methods=["GET"])
    def get_employee_by_dep(emp_id, dep_id):
        try:
            print("here")
            return es.get_employee_by_dep(emp_id, dep_id).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department/<dep_id>/employee", methods=["GET"])
    def get_all_employees_by_dep(dep_id):
        return jsonify([employee.json() for employee in es.get_all_employees_by_dep(dep_id)])
        # try:
        #     print("here")
        #     return es.get_all_employees_by_dep(dep_id).json(), 200
        # except ValueError as e:
        #     return "Not a valid ID", 400
        # except ResourceNotFound as r:
        #     return r.message, 404

    @app.route("/employee", methods=["POST"])
    def post_employee():
        body = request.json
        # print("here")
        employee = Employee(full_name=body["fullName"], email=body["email"], password=body["password"],
                            superv_id=body["supervId"], dep_id=body["depId"])
        employee = es.create_employee(employee)
        # print("here")
        print(employee)
        # print("here")
        return employee.json(), 201

    @app.route("/employee/<emp_id>", methods=["PUT"])
    def put_employee(emp_id):
        try:
            body = request.json
            employee = Employee(emp_id=emp_id, full_name=body["fullName"], email=body["email"],
                                password=body["password"], superv_id=body["supervId"], dep_id=body["depId"])

            employee = es.update_employee(employee)
            return employee.json(), 204

        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<emp_id>", methods=["DELETE"])
    def del_employee(emp_id):
        try:
            es.delete_employee(emp_id)
            return '', 204
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404


def _test():
    pass


if __name__ == '__main__':
    _test()
