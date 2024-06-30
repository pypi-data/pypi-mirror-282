
from scapy.packet import Packet
from scapy.fields import *
from .base_types import *
from .bit_fields import *
from .enums import *

class Composite(Packet):
    def extract_padding(self, s):
        return b'', s

class Decimal9Composite(Composite):
    name='Decimal9'
    fields_desc=[
        int64("mantissa"),
    ]
Decimal9 = lambda name: PacketField(name,Decimal9Composite(),Decimal9Composite)

class Decimal9NULLComposite(Composite):
    name='Decimal9NULL'
    fields_desc=[
        int64("mantissa"),
    ]
Decimal9NULL = lambda name: PacketField(name,Decimal9NULLComposite(),Decimal9NULLComposite)

class DecimalQtyComposite(Composite):
    name='DecimalQty'
    fields_desc=[
        int32("mantissa"),
    ]
DecimalQty = lambda name: PacketField(name,DecimalQtyComposite(),DecimalQtyComposite)

class FLOATComposite(Composite):
    name='FLOAT'
    fields_desc=[
        int64("mantissa"),
    ]
FLOAT = lambda name: PacketField(name,FLOATComposite(),FLOATComposite)

class MaturityMonthYearComposite(Composite):
    name='MaturityMonthYear'
    fields_desc=[
        uint16("year"),
        uint8("month"),
        uint8("day"),
        uint8("week"),
    ]
MaturityMonthYear = lambda name: PacketField(name,MaturityMonthYearComposite(),MaturityMonthYearComposite)

class PRICEComposite(Composite):
    name='PRICE'
    fields_desc=[
        int64("mantissa"),
    ]
PRICE = lambda name: PacketField(name,PRICEComposite(),PRICEComposite)

class PRICE9Composite(Composite):
    name='PRICE9'
    fields_desc=[
        int64("mantissa"),
    ]
PRICE9 = lambda name: PacketField(name,PRICE9Composite(),PRICE9Composite)

class PRICENULLComposite(Composite):
    name='PRICENULL'
    fields_desc=[
        int64("mantissa"),
    ]
PRICENULL = lambda name: PacketField(name,PRICENULLComposite(),PRICENULLComposite)

class PRICENULL9Composite(Composite):
    name='PRICENULL9'
    fields_desc=[
        int64("mantissa"),
    ]
PRICENULL9 = lambda name: PacketField(name,PRICENULL9Composite(),PRICENULL9Composite)

class groupSizeComposite(Composite):
    name='groupSize'
    fields_desc=[
        uint16("blockLength"),
        uint8("numInGroup"),
    ]
groupSize = lambda name: PacketField(name,groupSizeComposite(),groupSizeComposite)

class groupSize8ByteComposite(Composite):
    name='groupSize8Byte'
    fields_desc=[
        PadField(uint16("blockLength"),align=7),
        uint8("numInGroup"),
    ]
groupSize8Byte = lambda name: PacketField(name,groupSize8ByteComposite(),groupSize8ByteComposite)

class groupSizeEncodingComposite(Composite):
    name='groupSizeEncoding'
    fields_desc=[
        uint16("blockLength"),
        uint16("numInGroup"),
    ]
groupSizeEncoding = lambda name: PacketField(name,groupSizeEncodingComposite(),groupSizeEncodingComposite)

class messageHeaderComposite(Composite):
    name='messageHeader'
    fields_desc=[
        uint16("blockLength"),
        uint16("templateId"),
        uint16("schemaId"),
        uint16("version"),
    ]
messageHeader = lambda name: PacketField(name,messageHeaderComposite(),messageHeaderComposite)
