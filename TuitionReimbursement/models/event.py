class Event:

    def __init__(self, ev_id=0, event_type='', percentage=0):
        self.ev_id = ev_id
        self.event_type = event_type
        self.percentage = percentage

    def __repr__(self):
        return str({
            'ev_id': self.ev_id,
            'event_type': self.event_type,
            'percentage': self.percentage,
        })

    def json(self):
        return {
            'evId': self.ev_id,
            'eventType': self.event_type,
            'percentage': self.percentage,
        }
