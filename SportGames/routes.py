"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/football')
@view('football')
def football():
    """Renders the football page."""
    return dict(
        title='Football',
        message='Your football page.',
        year=datetime.now().year
    )

@route('/chess')
@view('chess')
def chess():
    """Renders the chess page."""
    return dict(
        title='Chess',
        message='Your chess page.',
        year=datetime.now().year
    )
