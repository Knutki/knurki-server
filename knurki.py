import os
from flask import Flask, redirect
from events import sources as events_sources
from events.usosweb.oauth import oauth_sources
from utils import SOURCES as _SOURCES

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']

def SOURCES(url):
    return _SOURCES(url, app)

SOURCES('api')(
    events_sources
)

SOURCES('')(
    oauth_sources
)


@app.route('/api')
def api_redirect_to_github():
    return redirect("https://github.com/Knutki/knurki-server")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
