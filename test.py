import os
import yaml
import json
from netmiko import ConnectHandler
from utils import router_loop
from utils import execute_show_commands
import getpass
import datetime

#time_now = datetime.datetime.now().isoformat(timespec="seconds")
user_name = input('username: ')
passwd = getpass.getpass('Please enter the password: ')

#Change the directory to the folder of the checks
os.chdir('/home/ibrahim/Documents/network_tools/')

#defining a variable for the folders of the checks
network_tools_list = os.listdir('/home/ibrahim/Documents/network_tools/')
print(network_tools_list)

#defining a variable for the working sheet
working_sheet = input('kindly select the working folder: ')

#opening the working sheet
with open(working_sheet , 'r') as file:
    working_doc_json = file.read()
    working_doc = json.loads(working_doc_json)
    real_working_doc =working_doc['check']

    #looping through indivial list  in the config_file
    for each in real_working_doc:
        #defining a variable for the hostname
        router_id = (each[0]['hostname'])
        #defining variable for the coammns
        config = (each[1]['command'])
        connection = ConnectHandler(**router_loop(router_id, user_name, passwd))
        connection.enable()
        print(f'logging in to {router_id}')
        #looping through each command
        for each_config in config:
            output = connection.send_command(each_config)
            print(output)
        connection.disconnect()
        #saving the output to a new folder in the  document file
        os.chdir('/home/ibrahim/Documents/script_output/')
        backup_dir = '/home/ibrahim/Documents/script_output/' + working_sheet
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir) i
        fo = open(backup_dir + '/' + router_id, 'w')
        fo.write(output)
        















