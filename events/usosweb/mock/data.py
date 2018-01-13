from datetime import datetime, timedelta
from events.event import Event
from events.usosweb.wutlocation import WUTLocation


def mock_data():
    subjects = [
        ("Matematyka Dyskretna", 212),
        ("Inżynieria Oprogramowania", 211),
        ("Analiza Matematyczna", 213),
        ("Teoria Informacji", 214)
    ]
    now = datetime.now().replace(second=0) - timedelta(hours=1, minutes=51)
    return [
        Event(
            name,
            now + timedelta(hours=2*i, minutes=5*i),
            now + timedelta(hours=2*(i+1), minutes=5*i),
            WUTLocation(
                "Mini",
                str(room)
            )
        ).as_dict()
        for i, (name, room) in enumerate(subjects)
    ]
