from bottle import post, request, template
from datetime import date, datetime
import json
import re


regexfordate = re.compile(r'\d{2}.\d{2}.\d{4}$')
regexfornickname = re.compile('[a-zA-Z1-9_\-]{2,20}')

def isValidDate(date):
    try:  
        if re.fullmatch(regexfordate, date):
            if(datetime.strptime(date, '%d.%m.%Y') <= datetime.now() and (datetime.now().year - datetime.strptime(date, '%d.%m.%Y').year < 25)):
                return True
        return False
    except:
        return False
    
def isValidNick(nick):
    if re.fullmatch(regexfornickname, nick):
        return True
    return False
         


@post('/articles', method='post')
def addarticle():
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    username = request.forms.get('USERNAME')
    link = request.forms.get('LINK')
    current_date = request.forms.get('DATE')
    if(len(title) < 8):
        return f"Incorrect title! The title of the article must be at least 8 characters long!" 
    elif(len(description) < 50 or len(description) > 200):
        return f"Incorrect description! The description of the article must be between 50 and 200 characters!" 
    elif(not isValidNick(username)):
        return f"Incorrect nickname! The nickname must be from 2 to 20 characters (without special characters)!" 
    elif(len(link) < 10):
        return f"Incorrect link! An existing link must be entered!" 
    elif(not isValidDate(current_date)):
        return f"Incorrect date! The date must be in the format \"dd.MM.yyyy\" and should not be outdated!" 
    

    try:
        # Пытаемся открыть файл "calchistory.json" для чтения
        with open("static\\articles.json", "r") as read_json:
            # Загружаем данные из файла в список articles
            articles = json.load(read_json)
    except FileNotFoundError:
            # Если файл не найден, создаем новый словарь history с пустыми списками для каждого алгоритма    
            articles = []
    except:
        articles = []


    articles.append({title:{'author': username, 'text': description, 'link': link, 'date': current_date}})
    if(articles != []):
        articles.sort(key=lambda x: x[list(x.keys())[0]]['date'], reverse=True)
    with open("static\\articles.json", 'w') as outfile:
        json.dump(articles, outfile, indent = 3)
    

    return template('articles.tpl',title='Articles',
        message='Your articles page.',
        year=datetime.now().year,
        data=articles)
