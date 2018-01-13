from datetime import datetime, timedelta
from events.event import Event
from events.usosweb.wutlocation import WUTLocation


def mock_data():
    subjects = [
        ("Teoria", 212),
        ("Programowanie", 211),
        ("Matematyka", 213),
        ("Filozofia", 214)
    ]
    now = datetime.now().replace(minute=0, second=0) - timedelta(hours=3)
    return [
        Event(
            name,
            now + timedelta(hours=2*i),
            now + timedelta(hours=2*(i+1)),
            WUTLocation(
                "Mini",
                str(room)
            )
        ).as_dict()
        for i, (name, room) in enumerate(subjects)
    ]
