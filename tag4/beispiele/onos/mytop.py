from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Add switches
        switchL1 = self.addSwitch('sL1', dpid='1')
        switchL2 = self.addSwitch('sL2', dpid='2')

        host1 = self.addHost('h1')
        host2 = self.addHost('h2')

        # Connect Switches
        self.addLink(switchL1, switchL2)

        # Connect Hosts
        self.addLink(host1, switchL1)
        self.addLink(host2, switchL2)


topos = {'mytopo': (lambda: MyTopo())}
