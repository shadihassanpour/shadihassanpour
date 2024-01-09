"""nornir_scrapli.tasks.send_commands"""
from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=send_commands_from_file, file="command_list")
print_result(results)


# def send_commands_from_file(task: Task,file: str)
# command_list : is name ot text-file that include of commands
