from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")
print(nr.inventory.hosts)
for group in nr.inventory.groups:
  print(nr.inventory.groups[group].data['community'])
for host in nr.inventory.hosts:
  print(nr.inventory.hosts[host].data['community'])


#comment:( we have host.yaml,group.yaml,default.yaml, config.yaml)
# when u want config, u need date for example : as num ?, neighbor ?, other data.
# save data in inventory and access this data.
# prioritize: first: host ,second: group , third:default .
# for add data u just write data at the same level hostname:# as below :
        hostnam:  "192.168.1.1"
           username: "zitel"
           password: "zitelzitel"
        data:
           community: zitel-co.ir
           router_id: 1.1.1.1
           neighbor_id: 192.168.1.2
#for access inventory just print (nr.inventory)
#for access list hosts in inventory print(nr.inventory.hosts)
# for access list groups in inventory print(nr.inventory.groups)
