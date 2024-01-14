from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
def snmp_config(task):
    task.run(task=send_config, config=f"snmp-server community {task.host['community']}")

results = nr.run(task=snmp_config)
print_result(results)


#comment
# we already khonw that we need data fo config devices ( access with inventory)
# for send config u must import send_config in nornir_scrapli.tasks 
# def send_config(task: Task,config: str,dru_run:optional(bool))
# dry_run just ,default= none ,check that config run on devices and apply it,if dry_run= true config apply.
# in header u must import send_config from nornir_scrapli.tasks
# function fstring:convert data to value 
#The community is a type of shared password between the SNMP management station and the device, which is used to authenticate the SNMP management station. Communities are only defined in SNMPv1 and v2 because SNMP v3 works with users instead of communities.
#
