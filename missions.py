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
def validation_check(list1):
    time = list1[1]
    category = list1[2]

