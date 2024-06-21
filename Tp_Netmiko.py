from netmiko import ConnectHandler

cisco1 = {
 "device_type": "cisco_nxos",
 "host": "sandbox-iosxr-1.cisco.com",
 "username": "admin",
 "password": "C1sco12345"
}
net_connect = ConnectHandler(**cisco1)
answer1 = net_connect.send_command("show running-config")
answer2 = net_connect.send_command("sh ip int br up") 
answer3 = net_connect.send_command("show ip interface brief down")
answer4 = net_connect.send_command("show ip route")
print(answer1, answer2, answer3, answer4)
net_connect.disconnect()
