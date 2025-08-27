import client

def create_task_dictionary():
    task = {}
    for condition in client.task_conditions:
        task[condition] = ""
    return task



# def convert_dict_to_byte(dict):
#     json_str = json.dumps(dict)
#     bytes_obj = bytes(json_str, 'utf-8')
#     return bytes_obj


def validation_check(task):
    time = task[1].split(" ")[0]
    letter = task[1].split(" ")[1].lower()
    category = task[2].lower()
    description = task[3]
    contact_details = task[4]

    if not time.isnumeric():
        print("Time must be numeric")
        return True
    elif letter != "m" or letter != "h" or letter != "d":
        print("letter must be 'm', 'h' or 'd'")
        return True
    elif category not in category_list:
        print("Category is not valid")
        return True
    elif len(description) > 100:
        print("Description is too long, max 100 characters")
        return True
    elif not contact_details.isnumeric():
        print("Contact details must be numeric")




    pass


