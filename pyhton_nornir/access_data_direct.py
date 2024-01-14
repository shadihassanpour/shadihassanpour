from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
def acc_data(task):
    print(task.host['community'])

results = nr.run(task=acc_data)
print_result(results)




#comment
#  task : any task 
#this task just print community in host part in hosts.yaml or groups.yaml or defaults.yaml (prioritize: first: host ,second: group , third:default )
# config.yaml ( contains of : plugin ,host_file,group_file,default_file)
