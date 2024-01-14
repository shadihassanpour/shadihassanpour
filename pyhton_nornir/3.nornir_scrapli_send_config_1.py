from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
for host in nr.inventory.hosts:
  results = nr.run(task=send_config, config=f"snmp-server community {nr.inventory.hosts[host].data['community']}")
  print_result(results)



#comment
# we already khonw that we need data fo config devices ( access with inventory)
# for send config u must import send_config in nornir_scrapli.tasks 
# def send_config(task: Task,config: str,dru_run:optional(bool))
# dry_run just check that config run on devices and does not apply.


