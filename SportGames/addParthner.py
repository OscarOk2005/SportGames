from bottle import datetime, post, request, template
from datetime import date
import json
import re

@post('/partners', method='post')

def addParthner():
    name = request.forms.get('name')
    description = "Brief description of " + name
    email = request.forms.get('email')
    phone = request.forms.get('telephone')
    start_date = request.forms.get('date_start')
    contract_term = request.forms.get('contract_term')
    contract_type = request.forms.get('con_type')
    number = 1
    partnerList = []
    with open('static\partner_companies.json', 'r', encoding='utf-8') as f:
        partnerList = json.load(f)
        number = partnerList["partner_companies_in_sports_sphere"][-1]["id"] + 1
        
    for partner in partnerList["partner_companies_in_sports_sphere"]:
        if (name in partner["name"]):
            return "The name is already used!"
    if (not checkEmal(email)):
        return "The email format is incorrect. E-mail should consist only of Latin letters, numbers and special characters, as well as have from 6 to 30 characters at the beginning and either @gmail.com , or @mail.ru, or yandex.ru at the end."
    if (not checkPhone(phone)):
        return "Incorrect phone! The phone must consist of 11 digits."
    if (not checkStart_date(start_date)):
        return "The date should not be earlier than the today."
    if not contract_term.isdigit():
        return "Contract term  must consist of only digits."
    if (checkContract_type(contract_type)):
        return "Contract type must selected of list."
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
    with open('static\partner_companies.json', 'w') as outfile:
        json.dump(partnerList, outfile, indent=4)
    """Renders the partners page."""
    return template(
        'partners.tpl',
        title='Partners',
        partner_companies=partnerList,
        message='Your partners page.',
        year=datetime.now().year
    )

def checkEmal(email):
    pattern = re.compile('[a-zA-Z0-9]{1}[a-zA-Z0-9._%+\-]{4,28}[a-zA-Z0-9]{1}@(gmail.com|mail.ru|yandex.ru)')
    return re.fullmatch(pattern, email)

def checkPhone(phone):
    if(phone[0] == '+' and len(phone) != 12):
        return False
    if (phone[0] != '+' and len(phone) != 11):
        return False
    x = re.search("^8|\+7{1}[\d]{10,11}$", phone)
    if x:
        return True
    else:
        return False

def checkStart_date(dastart_datete):
    try:
        regex = r'\d{4}-\d{2}-\d{2}$'
        if re.search(regex, dastart_datete):
            if(datetime.strptime(dastart_datete, '%Y-%m-%d') <= datetime.now() and datetime.strptime(dastart_datete, '%Y-%m-%d') >= datetime(1900, 1, 1)):
                return True
        return False
    except:
        return False
    
def checkContract_type(contract_type):
    if (contract_type == "Exclusive" or contract_type == "Non-exclusive"):
        return False
    else:
        return True