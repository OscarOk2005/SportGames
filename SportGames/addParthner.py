from bottle import post, request, template
from datetime import date
import json

@post('/parthners', method='post')

def addParthner():
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
        
    if(len(customer) < 4):
        return "Неккоректное имя"
    if(len(product) <= 2):
        return "Неккоректный товар"
    if(len(phone) != 11):
        return "Неккоректный телефон"
    if(len(address) < 20):
        return "Неккоректный адрес"
    orderList.append({"Number": number, "Customer" : customer,"Product":product, "Order date":  str(date.today()),"Phone": phone, "Address": address, "Delivery": str(delivery)})
    with open('static\orders.json', 'w') as outfile:
        json.dump(orderList, outfile, indent=4)
    return template('order.tpl',title='Orders',
        message='Your orders page.',
        year=date.now().year,
        data=orderList)




