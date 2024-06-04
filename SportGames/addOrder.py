from bottle import post, request, template
from datetime import date
import json
import re

@post('/orders', method='post')

def addOrder():
    # Получение данных
    customer = request.forms.get('Customer')
    product = request.forms.get('Product')
    phone = request.forms.get('Phone')
    address = request.forms.get('Address')
    delivery = request.forms.get('Delivery')
    number = 1
    orderList = []
    # Получение последнего номера
    with open('static\orders.json', 'r', encoding='utf-8') as f:
        orderList = json.load(f)
        number = orderList[-1]["Number"] + 1
    # Проверка имени
    if not checkCustomer(customer):
        return "Incorrect name"
    # Проверка товара
    if(len(product) <= 2):
        return "Incorrect product"
    # Проверка телефона
    if not checkPhone(phone):
        return "Incorrect phone"
    # Проверка адреса
    if(len(address) < 20):
        return "Incorrect address"
    # Добавление данных
    orderList.append({"Number": number, "Customer" : customer,"Product":product, "Order date":  str(date.today()),"Phone": phone, "Address": address, "Delivery": str(delivery)})
    # Сохранение изменений
    with open('static\orders.json', 'w') as outfile:
        json.dump(orderList, outfile, indent=4)
    # Перезагрузка страницы
    return template('order.tpl',title='Orders',
        message='Your orders page.',
        year=date.now().year,
        data=orderList)

def checkCustomer(customer):
    # Проверка наличия пробела
    if not (' 'in customer):
        return False
    # Проверка длины имени
    if(len(customer.split(' ')[1]) > 25 or len(customer.split(' ')[1]) < 3):
        return False
    # Проверка длины фамилии
    surname = customer.split(' ')[0]
    if(len(surname) > 35 or len(surname) < 3):
        return False
    # Проверка двойных фамилий
    if ('-' in surname):
        if(len(surname.split('-')[0]) < 2 or len(surname.split('-')[1]) < 2):
            return False
    # Создание регулярного выражения и проверка входной строки на соответствие
    x = re.search("^[a-z]{1,}[\-]{0,1}[a-z]{1,} [a-z]{1,}$", customer.lower())
    if x:
        return True
    else:
        return False

def checkPhone(phone):
    # Проверка длины телефона
    if(phone[0] == '+' and len(phone) != 12):
        return False
    if (phone[0] != '+' and len(phone) != 11):
        return False
    # Создание регулярного выражения и проверка входной строки на соответствие
    x = re.search("^[8|+7]{1}[\d]{10,11}$", phone)
    if x:
        return True
    else:
        return False