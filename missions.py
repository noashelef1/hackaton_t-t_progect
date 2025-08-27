import consts
import json

def create_task_dictionary():
    task_conditions = ["Title", "duration", "category", "description", "contact_details"]
    task = {}
    for condition in task_conditions:
        task[condition] = ""
    return task


def convert_dict_to_byte(dict):
    json_str = json.dumps(dict)
    bytes_obj = bytes(json_str, 'utf-8')
    return bytes_obj


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
    elif category not in consts.tasks_categories:
        print("Category is not valid")
        return True
    elif len(description) > 100:
        print("Description is too long, max 100 characters")
        return True
    elif not contact_details.isnumeric():
        print("Contact details must be numeric")
        return True
    elif len(contact_details) != 10:
        print("Contact details must be 10 characters")
        return True
    else:
        return False

def research_filter(missions_details_dict, users_filter_dict):
    missions_filtered_list = []

    for mission in missions_details_dict:
        for details in mission:
            if details in users_filter_dict.keys() and mission not in missions_filtered_list:
                missions_filtered_list.append(mission)

    return missions_filtered_list