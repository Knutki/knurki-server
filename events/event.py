from datetime import datetime
from events.location import Location


class Event:

    def __init__(self,
                 name: str,
                 start: datetime,
                 end: datetime,
                 location: Location,
                 type: str,
                 dateformat="%Y-%m-%d %H:%M"):
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.type = type
        self.format = dateformat

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "start": self.start.strftime(self.format),
            "end": self.end.strftime(self.format),
            "location": self.location.as_dict()
        }

    def __eq__(self, other):
        return self.name == other.name and str(self.start) == str(other.start)

    def __hash__(self):
        return self.name.__hash__() + self.start.__hash__()
