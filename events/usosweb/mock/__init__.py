from datetime import timedelta
from flask import Blueprint, jsonify
from events.usosweb.mock.data import mock_data, current_day_default_start_time

mock_blueprint = Blueprint('mock', __name__)


@mock_blueprint.route('/events/today')
def today_events():
    return jsonify(mock_data())


@mock_blueprint.route('/events/currentPeriod')
def current_period_events():
    WEEK = 7
    now = current_day_default_start_time()
    start = now - timedelta(days=now.weekday())
    return jsonify([
        {
            "date": (start.replace(hour=0, minute=0) + timedelta(days=i)).strftime("%Y-%m-%d %H:%M"),
            "events": mock_data(start + timedelta(days=i))
        } for i in range(2*WEEK)])
