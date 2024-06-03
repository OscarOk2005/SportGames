from bottle import post, request, template
from datetime import date
import json
import re

@post('/orders', method='post')

def addOrder():
    customer = request.forms.get('Customer')
    product = request.forms.get('Product')
    phone = request.forms.get('Phone')
    address = request.forms.get('Address')
    delivery = request.forms.get('Delivery')
    number = 1
    orderList = []
    with open('static\orders.json', 'r', encoding='utf-8') as f:
        orderList = json.load(f)
        number = orderList[-1]["Number"] + 1
        
    if(checkCustomer(customer)):
        return "Incorrect name"
    if(len(product) <= 2):
        return "Incorrect product"
    if(checkPhone(phone)):
        return "Incorrect phone"
    if(len(address) < 20):
        return "Incorrect address"
    orderList.append({"Number": number, "Customer" : customer,"Product":product, "Order date":  str(date.today()),"Phone": phone, "Address": address, "Delivery": str(delivery)})
    with open('static\orders.json', 'w') as outfile:
        json.dump(orderList, outfile, indent=4)
    return template('order.tpl',title='Orders',
        message='Your orders page.',
        year=date.now().year,
        data=orderList)

def checkCustomer(customer):
    if(len(customer) > 35 or len(customer) < 4):
        return False
    x = re.search("^[a-z]{1,}[\-]{0,1}[a-z]{1,}$", customer.lower())
    if x:
        return True
    else:
        return False

def checkPhone(phone):
    if(phone[0] == '+' and len(phone) != 12):
        return False
    elif (len(phone) != 11):
        return False
    x = re.search("^[8|+7]{1}[\d]{10,11}$", phone)
    if x:
        return True
    else:
        return False