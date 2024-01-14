"""nornir_scrapli.tasks.send_commands"""
from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=send_commands, commands=["sh int description ","sh run int Eth1/45"])
print_result(results)




#first you must import InitNornir for use config_file
# second you must import send_commands in nornir_scrapli.tasks
#def send_commands(task: Task,commands: List[str])   :  use template for cli commands
