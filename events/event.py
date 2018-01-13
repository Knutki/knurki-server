from datetime import datetime
from events.location import Location


class Event:

    def __init__(self,
                 name: str,
                 start: datetime,
                 end: datetime,
                 location: Location,
                 dateformat="%Y-%m-%d %H:%M"):
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.format = dateformat

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "start": self.start.strftime(self.format),
            "end": self.end.strftime(self.format),
            "location": self.location.as_dict()
        }
