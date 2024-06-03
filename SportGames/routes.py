"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import json
import addOrder
import addArticle

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
def articles():
    try:
        # Пытаемся открыть файл "calchistory.json" для чтения
        with open('static\\articles.json', 'r', encoding='utf-8') as read_json:
            # Загружаем данные из файла в список articles
            articles = json.load(read_json)
    except FileNotFoundError:
            # Если файл не найден, создаем новый словарь history с пустыми списками для каждого алгоритма    
            articles = []
    """Renders the about page."""
    print("NOR")
    return dict(
        title='Addarticle',
        message='Your application description page.',
        year=datetime.now().year,
        data=articles
    )
@route('/orders')
@view('orders')
def orders():
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
def partners():
    with open('static\partner_companies.json', 'r', encoding='utf-8') as f:
        partner_companies = json.load(f)
    """Renders the partners page."""
    return dict(
        title='Partners',
        partner_companies=partner_companies,
        message='Your partners page.',
        year=datetime.now().year
    )