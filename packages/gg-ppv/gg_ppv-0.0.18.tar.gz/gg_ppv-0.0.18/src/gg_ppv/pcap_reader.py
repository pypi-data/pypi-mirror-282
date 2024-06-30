from . import Mdp
from scapy.fields import *
from scapy.utils import rdpcap

import cocotb
import dpkt
import datetime
from dpkt.utils import mac_to_str, inet_to_str


class PCAPReader:
    def print_packets(self,pcap):
        """Print out information about each packet in a pcap

        Args:
            pcap: dpkt pcap reader object (dpkt.pcap.Reader)
        """
        # For each packet in the pcap process the contents
        for packet in pcap:

            # Print out the timestamp in UTC
            # print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(float(timestamp))))

            # Unpack the Ethernet frame (mac src/dst, ethertype)
            # eth = dpkt.ethernet.Ethernet(buf)
            # print('Ethernet Frame: ', mac_to_str(eth.src), mac_to_str(eth.dst), eth.type)

            # Make sure the Ethernet data contains an IP packet
            # if not isinstance(eth.data, dpkt.ip.IP):
                # print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
                # continue

            # Now access the data within the Ethernet frame (the IP packet)
            # Pulling out src, dst, length, fragment info, TTL, and Protocol
            # ip = eth.data

            # Print out the info, including the fragment flags and offset
            # print('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' %
                # (inet_to_str(ip.src), inet_to_str(ip.dst), ip.len, ip.ttl, ip.df, ip.mf, ip.offset))

            mdp = Mdp(packet)
            print(mdp)
            
        # # Pretty print the last packet
        # print('** Pretty print demo **\n')
        # eth.pprint()

    def read(self, path):
        """Open up a test pcap file and print out the packets"""
        with open(path, 'rb') as f:
            pcap = rdpcap(f)
            self.print_packets(pcap)
