int1 = {'ip': '10.0.0.1',
        'description': 'test1'}
int2 = {'ip': '10.0.0.2',
        'description': 'test2'}
int3 = {'ip': '10.0.0.3',
        'description': 'test3'}
int4 = {'ip': '10.0.0.4',
        'description': 'test4'}
int5 = {'ip': '10.0.0.5',
        'description': 'test4'}

r1 = {'hostname': 'dev1', 'version': 'aaaaaaaaaa1234',
      'interface': {'Ethernet': [int1, int2, int3, int4]}}

r2 = {'hostname': 'dev2', 'version': 'aaaaaaaaaa1233',
      'interface': {'Ethernet': [int2, int3, int5]}}

# Geben Sie für r1, und r2 alle ips aus und ermitteln Sie alle
# unterschiedlichen und gemeinsamen ips.
