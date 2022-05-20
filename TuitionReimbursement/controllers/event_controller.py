from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.event import Event
from repo.event_repo_impl import EventRepoImpl
from services.event_service import EventService

evr = EventRepoImpl()
evs = EventService(evr)


def route(app):
    @app.route("/event/<ev_id>", methods=["GET"])
    def get_event(ev_id):
        try:
            print("here")
            return evs.get_event_by_id(ev_id).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404


def _test():
    pass


if __name__ == '__main__':
    _test()
