

def create_task_dictionary():
    task_conditions = ["Title", "duration", "category", "description", "contact_details"]
    task = {}
    for condition in task_conditions:
        task[condition] = ""
    return task


# def convert_dict_to_byte(dict):
#     json_str = json.dumps(dict)
#     bytes_obj = bytes(json_str, 'utf-8')
#     return bytes_obj
