import requests
from lxml import etree
from credentials import username, password, ip

URL = "http://{}/ins".format(ip)
CRED = (username, password)

COMMAND = """<?xml version="1.0"?>
<ins_api>
  <version>1.0</version>
  <type>cli_show</type>
  <chunk>0</chunk>
  <sid>sid</sid>
  <input>sho int br</input>
  <output_format>xml</output_format>
</ins_api>"""

HDR = {'Content-type': 'application/xml',
       'Accept': 'application/xml'}

RESP = requests.post(URL, headers=HDR, auth=CRED, data=COMMAND)

RESP_PAYLOAD = RESP.text
print(RESP.status_code)
print(RESP.text)
print(type(RESP_PAYLOAD))
TREE = etree.fromstring(RESP_PAYLOAD)
print('List of Vlans for Access interfaces:')
for i in TREE.iter('ROW_interface'):
    interface = i.find('interface')
    print(interface)
