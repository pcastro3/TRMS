from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.department import Department
from repo.department_repo_impl import DepartmentRepoImpl
from services.department_service import DepartmentService

dr = DepartmentRepoImpl()
ds = DepartmentService(dr)


def route(app):
    @app.route("/department", methods=["GET"])
    def get_all_departments():
        return jsonify([department.json() for department in ds.get_all_departments()])

    @app.route("/department/<d_id>", methods=["GET"])
    def get_department(d_id):
        try:
            return ds.get_department_by_id(int(d_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department", methods=["POST"])
    def post_department():
        body = request.json

        department = Department(dep_head=body["depHead"], dep_name=body["depName"])
        department = ds.create_department(department)
        print(department)
        return department.json(), 201

    @app.route("/department/<d_id>", methods=["PUT"])
    def put_department(d_id):
        try:
            body = request.json
            department = Department(d_id=d_id, dep_head=body["depHead"], dep_name=body["depName"])

            department = ds.update_department(department)
            return department.json(), 204

        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department/<d_id>", methods=["DELETE"])
    def del_department(d_id):
        try:
            ds.delete_department(d_id)
            return '', 204
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404


def _test():
    pass


if __name__ == '__main__':
    _test()




