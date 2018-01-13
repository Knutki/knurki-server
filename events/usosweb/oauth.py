import os
from urllib.parse import urlencode

from flask_oauthlib.client import OAuth
from flask import session, Blueprint, url_for, request, flash, redirect

oauth_blueprint = Blueprint('oauth', __name__)

oauth = OAuth()

usos = oauth.remote_app(
    'usosweb',
    base_url='https://apps.usos.pw.edu.pl/',
    request_token_url="https://apps.usos.pw.edu.pl/services/oauth/request_token?" + urlencode({"scopes": "studies|offline_access"}),
    access_token_url='https://apps.usos.pw.edu.pl/services/oauth/access_token',
    authorize_url='https://apps.usos.pw.edu.pl/services/oauth/authorize',
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET']
)


@usos.tokengetter
def get_usosweb_token(token=None):
    return session.get('usosweb_token')


@oauth_blueprint.route('/login')
def login():
    return usos.authorize(
        callback=url_for(
            'oauth.oauth_authorized',
            next=request.args.get('next') or request.referrer or None
        )
    )


@oauth_blueprint.route('/oauth-authorized')
def oauth_authorized():
    next_url = request.args.get('next') or url_for('usos.get_user_info')
    resp = usos.authorized_response()
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['usosweb_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    return redirect(next_url)

oauth_sources = [oauth_blueprint]
