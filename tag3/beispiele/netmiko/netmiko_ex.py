# Kurzes Beispiel, für den Aufbau einer Verbindung zum einem klassischen
# Cisco-Device mit hilfe des pakets netmiko. Dieses baut selbst u. A. auf dem
# Paket paramiko auf was bei Bedarf generellere ssh-Verbindungen erlaubt.

from netmiko import ConnectHandler

# Dictionary mit allen Informationen zu Device und Verbindung
cisco_123 = {
    'device_type': 'cisco_nxos',
    'ip': '192.168.181.21',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,           # optional, Default: 22
    'secret': 'secret',     # optional, Default: ''
    'verbose': False,       # optional, Default: False
}

# Verbindungsaufbau über den Konstruktor der Klasse ConnectHandler. Das
# Dictionary wird hier verwendet um seinen Inhalt als Keyword-Arguments zu
# übergeben.
net_connect = ConnectHandler(**cisco_123)
# output = net_connect.send_command('show run')
# print(output)

output = net_connect.send_command('show version')
lines = output.split('\n')
print(type(lines), len(lines))
# print(lines)
for line in lines:
    if 'image' in line:
        start = line.find('bootflash:')
        print(line)
        print(start)
        print(line[start:])
