import json
from datetime import datetime

def get_all_operations(file_path):
    with open(file_path) as file:
        content = json.load(file)
    return content


def get_only_executed(operations):
    completed = []
    for operation in operations:
        if operation['state'] == 'EXECUTED':
            completed.append(operation)
    return completed


def sorting_operations_by_date(operations):
    sorting_date = sorted(operations,key=lambda operation: operation['date'], reversed=True)
    return sorting_date


def conversion_date(date):
    date_object = datetime.fromisoformat(date)
    date_str = date_object.strftime('%d.%m.%Y')
    return date_str


def hide_banking_details(banking_details: str):
    if banking_details.startswith('Счет'):
        result = f'Счет **{banking_details[-4:]}'
    else:
        components = banking_details.split()
        number = components[-1]
        hided_number = f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
        components[-1] = hided_number
        result = ' '.join(components)
    return result


def get_output_date(operation):
    date = formate_date(operation['date'])
    if operation.get('from'):
        from_where = hide_banking_details(operation.get('from'))
    else:
        from_where = ''
    to_where = hide_banking_details(operation.get('to'))

    return (f'{date} {operation['description']}\n'
            f'{from_where} -> {to_where}\n'
            f'{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}')






