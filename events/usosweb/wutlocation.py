from events.location import Location


class WUTLocation(Location):
    def __init__(self, faculty: str, room: str):
        self.faculty = faculty
        self.room = room

    def as_dict(self) -> dict:
        return {
            "faculty": self.faculty,
            "room": self.room
        }
