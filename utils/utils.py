import json


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




        #return sorted(date, key=lambda operation: operation['date'], reversed=True)


    #for state in date:
        #if state["state"] == condition:
            #return (state["state"])


