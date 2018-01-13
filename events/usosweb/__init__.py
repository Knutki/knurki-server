from datetime import timedelta, datetime
from flask import session, Blueprint, jsonify

from events.event import Event
from events.usosweb.oauth import usos
from events.usosweb.wutlocation import WUTLocation

usos_blueprint = Blueprint('usos', __name__)


@usos_blueprint.route("/user")
def get_user_info():
    return jsonify(usos.get("https://apps.usos.pw.edu.pl/services/users/user").data.copy())


@usos_blueprint.route("/events/currentPeriod")
def get_today_schedule():
    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    first_start = start.strftime("%Y-%m-%d")
    second_start = (start + timedelta(days=7)).strftime("%Y-%m-%d")
    usos_events = usos.get(
        "https://apps.usos.pw.edu.pl/services/tt/student",
        data={
            "start": first_start,
            "fields": "start_time|end_time|course_name|classtype_name|building_name|room_number"
        }
    ).data.copy() + usos.get(
        "https://apps.usos.pw.edu.pl/services/tt/student",
        data={
            "start": second_start,
            "fields": "start_time|end_time|course_name|classtype_name|building_name|room_number"
        }
    ).data.copy()

    events = [
        Event(
            event['course_name']['pl'],
            datetime.strptime(event['start_time'], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(event['end_time'], "%Y-%m-%d %H:%M:%S"),
            WUTLocation(
                event["building_name"]["pl"],
                event["room_number"]
            ),
            event['classtype_name']['pl']
        )
        for event in usos_events
    ]

    def get_formatted_delta(days):
        return (start + timedelta(days=days)).strftime("%Y-%m-%d")

    day_events = [
        {
            "date": get_formatted_delta(i),
            "events": [event.as_dict() for event in events if event.start.strftime("%Y-%m-%d") == get_formatted_delta(i)]
        }
        for i in range(14)
    ]
    return jsonify(day_events)
