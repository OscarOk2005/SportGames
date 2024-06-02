"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import json
import addOrder

@route('/')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        title='Homepage',
        message='Your football page.',
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

@route('/articles')
@view('articles')
def chess():
    """Renders the articles page."""
    return dict(
        title='Articles',
        message='Your articles page.',
        year=datetime.now().year
    )

@route('/orders')
@view('orders')
def chess():
    with open('static\orders.json', 'r', encoding='utf-8') as f:
        orderList = json.load(f)
    """Renders the orders page."""
    return dict(
        title='Orders',
        message='Your orders page.',
        year=datetime.now().year,
        data=orderList
    )


@route('/partners')
@view('partners')
def chess():
    """Renders the partners page."""
    return dict(
        title='Partners',
        message='Your partners page.',
        year=datetime.now().year
    )
