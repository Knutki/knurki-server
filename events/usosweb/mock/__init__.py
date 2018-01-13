from flask import Blueprint, jsonify
from events.usosweb.mock.data import mock_data

mock_blueprint = Blueprint('mock', __name__)


@mock_blueprint.route('/events/today')
def today_events():
    return jsonify(mock_data())
