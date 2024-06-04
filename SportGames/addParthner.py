# Импортируем необходимые модули и функции
from bottle import datetime, post, request, template
from datetime import date
import json
import re

# Определяем функцию-обработчик для POST-запроса на добавление партнера
@post('/partners', method='post')
def addParthner():
    # Получаем значения полей формы из запроса
    name = request.forms.get('name')
    description = "Brief description of " + name
    email = request.forms.get('email')
    phone = request.forms.get('telephone')
    start_date = request.forms.get('date_start')
    contract_term = request.forms.get('contract_term')
    contract_type = request.forms.get('con_type')
    # Обнуляем счетчик для номера партнера
    number = 1
    # Открываем файл с партнерами для чтения и загружаем его содержимое в список
    with open('static\partner_companies.json', 'r', encoding='utf-8') as f:
        partnerList = json.load(f)
        # Получаем номер нового партнера, увеличивая на 1 номер последнего партнера в списке
        number = partnerList["partner_companies_in_sports_sphere"][-1]["id"] + 1

    # Проверяем, нет ли уже партнера с таким же именем
    for partner in partnerList["partner_companies_in_sports_sphere"]:
        if (name in partner["name"]):
            # Если такой партнер уже есть, возвращаем сообщение об ошибке
            return "The name is already used!"

    # Проверяем корректность введенных данных
    if (not checkEmal(email)):
        # Если адрес электронной почты некорректен, возвращаем сообщение об ошибке
        return "The email format is incorrect. E-mail should consist only of Latin letters, numbers and special characters, as well as have from 6 to 30 characters at the beginning and either @gmail.com , or @mail.ru, or yandex.ru at the end."

    if (not checkPhone(phone)):
        # Если номер телефона некорректен, возвращаем сообщение об ошибке
        return "Incorrect phone! The phone must consist of 11 digits."

    if (not checkStart_date(start_date)):
        # Если дата начала партнерства некорректна, возвращаем сообщение об ошибке
        return "The date should not be earlier than the today."

    if not contract_term.isdigit():
        # Если срок контракта не является целым числом, возвращаем сообщение об ошибке
        return "Contract term  must consist of only digits."

    if (checkContract_type(contract_type)):
        # Если тип контракта не выбран из списка, возвращаем сообщение об ошибке
        return "Contract type must selected of list."

    # Добавляем нового партнера в список
    partnerList["partner_companies_in_sports_sphere"].append({
        "id": number,
        "name" : name,
        "description":description,
        "email": email,
        "phone": phone,
        "partnership_details": {
            "start_date": start_date,
            "contract_term": contract_term,
            "contract_type": contract_type,
        }})

    # Открываем файл с партнерами для записи и сохраняем в нем обновленный список
    with open('static\partner_companies.json', 'w') as outfile:
        json.dump(partnerList, outfile, indent=4)

    # Возвращаем шаблон страницы с партнерами
    return template(
        'partners.tpl',
        title='Partners',
        partner_companies=partnerList,
        message='Your partners page.',
        year=datetime.now().year
    )

# Функция для проверки корректности email
def checkEmal(email):
    # Регулярное выражение для проверки email
    pattern = re.compile('[a-zA-Z0-9]{1}[a-zA-Z0-9._%+\-]{4,28}[a-zA-Z0-9]{1}@(gmail.com|mail.ru|yandex.ru)')
    # Проверяем, соответствует ли email регулярному выражению, и возвращаем результат
    return re.fullmatch(pattern, email)

# Функция для проверки корректности номера телефона
def checkPhone(phone):
    # Проверяем, что номер начинается с '+' и имеет длину 12 символов, или что номер не начинается с '+' и имеет длину 11 символов
    if (phone[0] == '+' and len(phone) != 12) or (phone[0] != '+' and len(phone) != 11):
        # Если номер не соответствует требованиям, возвращаем False
        return False
    # Регулярное выражение для проверки номера телефона
    x = re.search("^8|\+7{1}[\d]{10,11}$", phone)
    # Проверяем, соответствует ли номер регулярному выражению, и возвращаем результат
    if x:
        return True
    else:
        return False

# Функция для проверки корректности даты начала партнерства
def checkStart_date(dastart_datete):
    # Пытаемся преобразовать дату в формат, соответствующий регулярному выражению
    try:
        regex = r'\d{4}-\d{2}-\d{2}$'
        if re.search(regex, dastart_datete):
            # Если дата соответствует регулярному выражению, проверяем, что она не раньше 1900 года и не позже текущей даты
            if (datetime.strptime(dastart_datete, '%Y-%m-%d') <= datetime.now() and datetime.strptime(dastart_datete, '%Y-%m-%d') >= datetime(1900, 1, 1)):
                return True
            else:
                return False
        else:
            # Если дата не соответствует регулярному выражению, возвращаем False
            return False
    except:
        # Если возникла ошибка при преобразовании даты, возвращаем False
        return False

# Функция для проверки корректности типа контракта
def checkContract_type(contract_type):
    # Проверяем, что тип контракта равен одному из двух допустимых значений
    if (contract_type == "Exclusive" or contract_type == "Non-exclusive"):
        # Если тип контракта допустим, возвращаем False (т.к. ошибки нет)
        return False
    else:
        # Если тип контракта недопустим, возвращаем True (т.к. есть ошибка)
        return True
