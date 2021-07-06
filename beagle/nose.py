import socket
import sys

from beagle import color
from ipaddress import IPv4Address, IPv6Address

class Frame():

    network_protocols = {
        '0800':'IPv4',
        '86DD':'IPv6'
    }

    def __init__(self, frame):
        '''Parsed based on the ethernet format.'''
        self.dst_mac = frame[:6].hex()
        self.src_mac = frame[6:12].hex()
        try:
            self.network_protocol = self.network_protocols[frame[12:14].hex()]
        except:
            self.network_protocol = ''
        self.datagram = frame[14:]

class Datagram():

    transport_protocols = {
        1:'ICMP',
        6:'TCP',
       17:'UDP'
    }

    def __init__(self, datagram, protocol):
        '''Parse based on network protocol format.'''
        self.protocol = protocol
        self.header_length = (datagram[0] & 15) * 4
        try:
            self.transport_protocol = self.transport_protocols[datagram[9]]
        except:
            self.transport_protocol = ''
        if protocol == 'IPv4':
            self.src_ip = IPv4Address(datagram[12:16])
            self.dst_ip = IPv4Address(datagram[16:20])
        if protocol == 'IPv6':
            self.src_ip = IPv6Address(datagram[12:16])
            self.dst_ip = IPv6Address(datagram[16:20])
        self.segment = datagram[self.header_length:]

class Segment():
    def __init__(self, segment, protocol):
        '''Parsed based on transport protocol format.'''
        self.protocol = protocol
        self.src_port = int(segment[:2].hex(), 16)
        self.dst_port = int(segment[2:4].hex(), 16)
        if protocol == 'TCP':
            self.header_length = (segment[12] >> 4 & 15) * 4
        if protocol == 'UDP':
            self.header_length = segment[4:6] * 4
        self.data = segment[self.header_length:]

class Nose():
    def __init__(self, interface):
        self.interface = interface
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    def sniff(self):
        try:
            self.socket.bind((self.interface, 3))
        except OSError:
            color.error(f'Cannot bind to the interface: {self.interface}.')
            sys.exit()
        color.success(f'Sniffing {self.interface}')
        while True:
            frame = Frame(self.socket.recv(2048))
            if not frame.network_protocol:
                color.verbose('Unkown network protocol', color.error)
                continue
            datagram = Datagram(frame.datagram, frame.network_protocol)
            if not datagram.transport_protocol:
                color.verbose('Unkown transport protocol', color.error)
                continue
            segment = Segment(datagram.segment, datagram.transport_protocol)
            color.verbose(f'{segment.protocol}://{datagram.src_ip}:{segment.src_port}/', color.normal)
            data = segment.data
            color.verbose(f'{str(data)}', color.normal)
