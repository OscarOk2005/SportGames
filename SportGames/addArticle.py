from bottle import post, request, template
from datetime import date, datetime
import json
import re

# регулярное выражение для проверки даты в формате "дд.мм.гггг"
regexfordate = re.compile(r'\d{2}.\d{2}.\d{4}$')
# регулярное выражение для проверки никнейма в формате от 2 до 20 символов, разрешены буквы, цифры,
#  нижнее подчеркивание и дефис
regexfornickname = re.compile('[a-zA-Z1-9_\-]{2,20}')

# функция для проверки корректности даты
def isValidDate(date):
    try:  
        if re.fullmatch(regexfordate, date):
            # проверяем, что дата не позже текущей и не старше 25 лет
            if(datetime.strptime(date, '%d.%m.%Y') <= datetime.now() 
               and (datetime.now().year - datetime.strptime(date, '%d.%m.%Y').year < 25)):
                return True
        return False
    except:
        return False
    
# функция для проверки корректности никнейма
def isValidNick(nick):
    if re.fullmatch(regexfornickname, nick):
        return True
    return False
         

# декоратор для функции addarticle, указывающий, что она обрабатывает POST-запросы на адрес "/articles"
@post('/articles', method='post')
# функция для добавления статьи
def addarticle():
    #создание переменных, в которые считываются данные полей ввода
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    username = request.forms.get('USERNAME')
    link = request.forms.get('LINK')
    current_date = request.forms.get('DATE')
    # проверяем, что длина заголовка не менее 8 символов
    if(len(title) < 8):
        return f"Incorrect title! The title of the article must be at least 8 characters long!" 
    # проверяем, что длина описания не менее 50 и не более 350 символов
    elif(len(description) < 20 or len(description) > 350):
        return f"Incorrect description! The description of the article must be between 20 and 350 characters!" 
    # проверяем, что никнейм корректен
    elif(not isValidNick(username)):
        return f"Incorrect nickname! The nickname must be from 2 to 20 characters (without special characters)!" 
    # проверяем, что длина ссылки не менее 10 символов
    elif(len(link) < 10):
        return f"Incorrect link! An existing link must be entered!" 
    # проверяем, что дата корректна
    elif(not isValidDate(current_date)):
        return f"Incorrect date! The date must be in the format \"dd.MM.yyyy\" and should not be outdated!" 
    

    try:
        # открываем файл "articles.json" для чтения
        with open("static\\articles.json", "r") as read_json:
            # Загружаем данные из файла в список articles
            articles = json.load(read_json)
    except FileNotFoundError:
            # Если файл не найден, создаем новый список articles    
            articles = []
    except:
        articles = []

    # добавляем новую статью в список articles
    articles.append({title:{'author': username, 'text': description, 'link': link, 'date': current_date}})
    # проверяем, что список articles не пустой
    if(articles != []):
        # сортируем список articles по дате в обратном порядке
        articles.sort(key=lambda x: x[list(x.keys())[0]]['date'], reverse=True)
    # открываем файл "articles.json" для записи.
    with open("static\\articles.json", 'w') as outfile:
        # записываем данные из списка articles в файл
        json.dump(articles, outfile, indent = 3)
    
    # возвращаем шаблон articles.tpl с данными для отображения на странице
    return template('articles.tpl',title='Articles',
        message='Your articles page.',
        year=datetime.now().year,
        data=articles)
