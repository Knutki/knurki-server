from datetime import datetime, timedelta
from events.event import Event
from events.usosweb.wutlocation import WUTLocation


def current_day_default_start_time():
    return datetime.now().replace(second=0) - timedelta(hours=2, minutes=1)


def mock_data(start=None):
    if start is None:
        start = current_day_default_start_time()
    subjects = [
        ("Matematyka Dyskretna", 212),
        ("Inżynieria Oprogramowania", 211),
        ("Analiza Matematyczna", 213),
        ("Teoria Informacji", 214)
    ]
    return [
        Event(
            name,
            start + timedelta(hours=2*i, minutes=5*i),
            start + timedelta(hours=2*(i+1), minutes=5*i),
            WUTLocation(
                "Mini",
                str(room)
            )
        ).as_dict()
        for i, (name, room) in enumerate(subjects)
    ]
