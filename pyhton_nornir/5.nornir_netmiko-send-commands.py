from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def netmiko_send_commands_example(task):
    task.run(task=netmiko_send_command, command_string="show int descr")

results=nr.run(task=netmiko_send_commands_example)
print_result(results)



#def netmiko_send_command(task: Task,command_string: str)
# you can see Supported Platforms (https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md)
# notice: u just type 1 command ,for more than one u must creat( for loop and list) as below:

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
commands=["show int descr ", "show run | inc ip route "]

def netmiko_send_commands_example(task):
    for command in commands:
        task.run(task=netmiko_send_command, command_string=command)

results=nr.run(task=netmiko_send_commands_example)
print_result(results)
