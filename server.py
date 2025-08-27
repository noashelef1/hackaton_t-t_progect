import socket
import json

task_conditions = ["name","duration","Tier"]
task = {task_conditions[0]: "X" , task_conditions[1]: "", task_conditions[2]: ""}
message = ""
def get_item_details():
    global message
    for i in range(len(task_conditions)):
        print("enter the item's " + task_conditions[i])
        message = input(" -> ")  # take input
        task[task_conditions[i]] = message
    return message

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server


    get_item_details()
    json_str = json.dumps(task)
    bytes_obj = bytes(json_str, 'utf-8')


    adding_another_item = "YES"
    while adding_another_item == 'YES':
        client_socket.send(bytes_obj)
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        adding_another_item = input("enter 'YES' to add another item")
        get_item_details()
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()