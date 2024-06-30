from scapy.fields import *
from scapy.packet import Packet
from .composite_base_types import messageHeader,messageHeaderComposite
from .base_types import *
from .layers import *

class Mdp(Packet):
    name = 'Mdp'
    fields_desc = [
        LEIntField('MsgSeqNum',default=0),
        LELongField('SendingTime',default=0),
        LEShortField("MsgSize",default=0),
        LEShortField("blockLength",default=0),
        LEShortField("templateId",default=0),
        LEShortField("schemaId",default=0),
        LEShortField("version",default=0)
    ]

    def guess_payload_class(self, payload):
        if(self.templateId in packet_ids.keys()):
            return packet_ids[self.templateId]['layer']
        else:
            return Packet.guess_payload_class(self, payload)

for key,value in packet_ids.items():
    bind_layers(Mdp, value['layer'],templateId=key,blockLength=value['blockLength'])
