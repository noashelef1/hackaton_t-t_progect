import socket
import json
import missions

task_conditions = ["Title","duration","category","description","contact_details"]
task = missions.create_task_dictionary()
message = ""
def get_task_details():
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


    get_task_details()
    json_str = json.dumps(task)
    bytes_obj = bytes(json_str, 'utf-8')
    client_socket.send(bytes_obj)
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + data)  # show in terminal
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()