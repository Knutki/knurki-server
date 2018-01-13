from flask import Flask
from events import sources as events_sources
from utils import SOURCES

app = Flask(__name__)

sources = SOURCES(app)(
    events_sources
)

if __name__ == '__main__':
    app.run(host="51.15.78.247", port=8888)
