from controllers import department_controller, employee_controller, request_controller, event_controller


def route(app):
    department_controller.route(app)
    employee_controller.route(app)
    request_controller.route(app)
    event_controller.route(app)
