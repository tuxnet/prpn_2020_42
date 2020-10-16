from time import time
from netmiko import ConnectHandler
import credentials as cred

device1 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip,
    'username': cred.username,
    'password': cred.password,
    'port': cred.port,
}

device2 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip2,
    'username': cred.username2,
    'password': cred.password2,
    'port': cred.port2,
}

device3 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip3,
    'username': cred.username3,
    'password': cred.password3,
    'port': cred.port3,
}

device4 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip4,
    'username': cred.username4,
    'password': cred.password4,
    'port': cred.port4,
}

device_list = [device1, device2, device3, device4]

for dev in device_list:
    net_connect = ConnectHandler(**dev)
    host = dev['ip']
    print(host, '... connected')
    config = net_connect.send_command('show run')
    # print(config)
    filename = host.replace(".w", "_") + '_' + str(time()) + '.config'
    cfg_file = open(filename, 'w')
    for line in config:
        cfg_file.write(line)
    cfg_file.close()
