
from scapy.fields import *
from scapy.layers import inet
from scapy.packet import Packet, bind_layers
from .base_types import *
from .bit_fields import *
from .enums import *
from .composite_base_types import *

class PaddedPacketListField(PacketField):
    __slots__ = ["count_from", "length_per_packet"]
    islist = 1

    def __init__(self, name, default, pkt_cls=None, count_from=None, length_per_packet=None):  # noqa: E501
        if default is None:
            default = []  # Create a new list for each instance
        PacketField.__init__(self, name, default, pkt_cls)
        self.count_from = count_from
        self.length_per_packet = length_per_packet

    def any2i(self, pkt, x):
        if not isinstance(x, list):
            return [x]
        else:
            return x

    def i2count(self, pkt, val):
        if isinstance(val, list):
            return len(val)
        return 1

    def i2len(self, pkt, val):
        if self.length_per_packet is not None:
            return len(p)*self.length_per_packet
        else:
            return sum(len(p) for p in val)

    def do_copy(self, x):
        if x is None:
            return None
        else:
            return [p if isinstance(p, (str, bytes)) else p.copy() for p in x]

    def getfield(self, pkt, s):
        c = pkt_cls = None
        if self.count_from is not None:
            c = self.count_from(pkt)

        lst = []
        ret = b""
        remain = s
        while remain:
            if self.length_per_packet is not None:
                pkt_buf = remain[0:self.length_per_packet]
            if c is not None:
                if c <= 0:
                    break
                c -= 1
            try:
                if pkt_cls is not None:
                    p = pkt_cls(pkt_buf)
                else:
                    p = self.m2i(pkt, pkt_buf)
            except Exception:
                if conf.debug_dissector:
                    raise
                p = conf.raw_layer(load=pkt_buf)
                remain = b""
            else:
                if self.length_per_packet is not None:
                    remain = remain[self.length_per_packet:]
                elif conf.padding_layer in p:
                    pad = p[conf.padding_layer]
                    remain = pad.load
                    del(pad.underlayer.payload)
                    if self.next_cls_cb is not None:
                        pkt_cls = self.next_cls_cb(pkt, lst, p, pkt_buf)
                        if pkt_cls is not None:
                            c = 0 if c is None else c
                            c += 1
                else:
                    remain = b""
            lst.append(p)
        return remain + ret, lst

    def addfield(self, pkt, s, val):
        if(self.length_per_packet is not None):
            return s + b"".join(bytes_encode(v) + (self.length_per_packet-len(bytes_encode(v)))*b"\0" for v in val)
        else:
            return s + b"".join(bytes_encode(v) for v in val)
class ChannelReset(Packet):
    name = 'ChannelReset'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=9)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            MDUpdateTypeNew('MDUpdateAction'),
            MDEntryTypeChannelReset('MDEntryType'),
            Int16('ApplID'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 2),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=2),
    ]
class AdminHeartbeat(Packet):
    name = 'AdminHeartbeat'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=0)
    
    fields_desc = [
    ]
class AdminLogin(Packet):
    name = 'AdminLogin'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            Int8('HeartBtInt'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=1)
    
    fields_desc = [
        blockPadded,
    ]
class AdminLogout(Packet):
    name = 'AdminLogout'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            Text('Text'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=180)
    
    fields_desc = [
        blockPadded,
    ]
class MDInstrumentDefinitionFuture(Packet):
    name = 'MDInstrumentDefinitionFuture'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            MatchEventIndicator('MatchEventIndicator'),
            uInt32NULL('TotNumReports'),
            SecurityUpdateAction('SecurityUpdateAction'),
            uInt64('LastUpdateTime'),
            SecurityTradingStatus('MDSecurityTradingStatus'),
            Int16('ApplID'),
            uInt8('MarketSegmentID'),
            uInt8('UnderlyingProduct'),
            SecurityExchange('SecurityExchange'),
            SecurityGroup('SecurityGroup'),
            Asset('Asset'),
            Symbol('Symbol'),
            Int32('SecurityID'),
            SecurityIDSource('SecurityIDSource'),
            SecurityType('SecurityType'),
            CFICode('CFICode'),
            MaturityMonthYear('MaturityMonthYear'),
            Currency('Currency'),
            Currency('SettlCurrency'),
            CHAR('MatchAlgorithm'),
            uInt32('MinTradeVol'),
            uInt32('MaxTradeVol'),
            PRICE9('MinPriceIncrement'),
            Decimal9('DisplayFactor'),
            uInt8NULL('MainFraction'),
            uInt8NULL('SubFraction'),
            uInt8NULL('PriceDisplayFormat'),
            UnitOfMeasure('UnitOfMeasure'),
            Decimal9NULL('UnitOfMeasureQty'),
            PRICENULL9('TradingReferencePrice'),
            SettlPriceType('SettlPriceType'),
            Int32NULL('OpenInterestQty'),
            Int32NULL('ClearedVolume'),
            PRICENULL9('HighLimitPrice'),
            PRICENULL9('LowLimitPrice'),
            PRICENULL9('MaxPriceVariation'),
            Int32NULL('DecayQuantity'),
            LocalMktDate('DecayStartDate'),
            Int32NULL('OriginalContractSize'),
            Int32NULL('ContractMultiplier'),
            Int8NULL('ContractMultiplierUnit'),
            Int8NULL('FlowScheduleType'),
            PRICENULL9('MinPriceIncrementAmount'),
            UserDefinedInstrument('UserDefinedInstrument'),
            LocalMktDate('TradingReferenceDate'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=216)
    
    class EventsPacket(Packet):
        name = 'Events'
        fields_desc = [
            EventType('EventType'),
            uInt64('EventTime'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class MDFeedTypesPacket(Packet):
        name = 'MDFeedTypes'
        fields_desc = [
            MDFeedType('MDFeedType'),
            Int8('MarketDepth'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class InstAttribPacket(Packet):
        name = 'InstAttrib'
        fields_desc = [
            InstAttribType('InstAttribType'),
            InstAttribValue('InstAttribValue'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class LotTypeRulesPacket(Packet):
        name = 'LotTypeRules'
        fields_desc = [
            Int8('LotType'),
            DecimalQty('MinLotSize'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('EventsBlockSize', 9),
        FieldLenField('EventsCount', None, fmt='<B', count_of='Events'),
        PaddedPacketListField('Events',[],EventsPacket,count_from=lambda pkt: pkt.EventsCount,length_per_packet=9),
        LEShortField('MDFeedTypesBlockSize', 4),
        FieldLenField('MDFeedTypesCount', None, fmt='<B', count_of='MDFeedTypes'),
        PaddedPacketListField('MDFeedTypes',[],MDFeedTypesPacket,count_from=lambda pkt: pkt.MDFeedTypesCount,length_per_packet=4),
        LEShortField('InstAttribBlockSize', 4),
        FieldLenField('InstAttribCount', None, fmt='<B', count_of='InstAttrib'),
        PaddedPacketListField('InstAttrib',[],InstAttribPacket,count_from=lambda pkt: pkt.InstAttribCount,length_per_packet=4),
        LEShortField('LotTypeRulesBlockSize', 5),
        FieldLenField('LotTypeRulesCount', None, fmt='<B', count_of='LotTypeRules'),
        PaddedPacketListField('LotTypeRules',[],LotTypeRulesPacket,count_from=lambda pkt: pkt.LotTypeRulesCount,length_per_packet=5),
    ]
class MDInstrumentDefinitionSpread(Packet):
    name = 'MDInstrumentDefinitionSpread'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            MatchEventIndicator('MatchEventIndicator'),
            uInt32NULL('TotNumReports'),
            SecurityUpdateAction('SecurityUpdateAction'),
            uInt64('LastUpdateTime'),
            SecurityTradingStatus('MDSecurityTradingStatus'),
            Int16('ApplID'),
            uInt8('MarketSegmentID'),
            uInt8NULL('UnderlyingProduct'),
            SecurityExchange('SecurityExchange'),
            SecurityGroup('SecurityGroup'),
            Asset('Asset'),
            Symbol('Symbol'),
            Int32('SecurityID'),
            SecurityIDSource('SecurityIDSource'),
            SecurityType('SecurityType'),
            CFICode('CFICode'),
            MaturityMonthYear('MaturityMonthYear'),
            Currency('Currency'),
            SecuritySubType('SecuritySubType'),
            UserDefinedInstrument('UserDefinedInstrument'),
            CHAR('MatchAlgorithm'),
            uInt32('MinTradeVol'),
            uInt32('MaxTradeVol'),
            PRICENULL9('MinPriceIncrement'),
            Decimal9('DisplayFactor'),
            uInt8NULL('PriceDisplayFormat'),
            PRICENULL9('PriceRatio'),
            Int8NULL('TickRule'),
            UnitOfMeasure('UnitOfMeasure'),
            PRICENULL9('TradingReferencePrice'),
            SettlPriceType('SettlPriceType'),
            Int32NULL('OpenInterestQty'),
            Int32NULL('ClearedVolume'),
            PRICENULL9('HighLimitPrice'),
            PRICENULL9('LowLimitPrice'),
            PRICENULL9('MaxPriceVariation'),
            uInt8NULL('MainFraction'),
            uInt8NULL('SubFraction'),
            LocalMktDate('TradingReferenceDate'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=195)
    
    class EventsPacket(Packet):
        name = 'Events'
        fields_desc = [
            EventType('EventType'),
            uInt64('EventTime'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class MDFeedTypesPacket(Packet):
        name = 'MDFeedTypes'
        fields_desc = [
            MDFeedType('MDFeedType'),
            Int8('MarketDepth'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class InstAttribPacket(Packet):
        name = 'InstAttrib'
        fields_desc = [
            InstAttribType('InstAttribType'),
            InstAttribValue('InstAttribValue'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class LotTypeRulesPacket(Packet):
        name = 'LotTypeRules'
        fields_desc = [
            Int8('LotType'),
            DecimalQty('MinLotSize'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class LegsPacket(Packet):
        name = 'Legs'
        fields_desc = [
            Int32('LegSecurityID'),
            SecurityIDSource('LegSecurityIDSource'),
            LegSide('LegSide'),
            Int8('LegRatioQty'),
            PRICENULL9('LegPrice'),
            DecimalQty('LegOptionDelta'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('EventsBlockSize', 9),
        FieldLenField('EventsCount', None, fmt='<B', count_of='Events'),
        PaddedPacketListField('Events',[],EventsPacket,count_from=lambda pkt: pkt.EventsCount,length_per_packet=9),
        LEShortField('MDFeedTypesBlockSize', 4),
        FieldLenField('MDFeedTypesCount', None, fmt='<B', count_of='MDFeedTypes'),
        PaddedPacketListField('MDFeedTypes',[],MDFeedTypesPacket,count_from=lambda pkt: pkt.MDFeedTypesCount,length_per_packet=4),
        LEShortField('InstAttribBlockSize', 4),
        FieldLenField('InstAttribCount', None, fmt='<B', count_of='InstAttrib'),
        PaddedPacketListField('InstAttrib',[],InstAttribPacket,count_from=lambda pkt: pkt.InstAttribCount,length_per_packet=4),
        LEShortField('LotTypeRulesBlockSize', 5),
        FieldLenField('LotTypeRulesCount', None, fmt='<B', count_of='LotTypeRules'),
        PaddedPacketListField('LotTypeRules',[],LotTypeRulesPacket,count_from=lambda pkt: pkt.LotTypeRulesCount,length_per_packet=5),
        LEShortField('LegsBlockSize', 18),
        FieldLenField('LegsCount', None, fmt='<B', count_of='Legs'),
        PaddedPacketListField('Legs',[],LegsPacket,count_from=lambda pkt: pkt.LegsCount,length_per_packet=18),
    ]
class SecurityStatus(Packet):
    name = 'SecurityStatus'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            SecurityGroup('SecurityGroup'),
            Asset('Asset'),
            Int32NULL('SecurityID'),
            LocalMktDate('TradeDate'),
            MatchEventIndicator('MatchEventIndicator'),
            SecurityTradingStatus('SecurityTradingStatus'),
            HaltReason('HaltReason'),
            SecurityTradingEvent('SecurityTradingEvent'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=30)
    
    fields_desc = [
        blockPadded,
    ]
class MDIncrementalRefreshBook(Packet):
    name = 'MDIncrementalRefreshBook'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            PRICENULL9('MDEntryPx'),
            Int32NULL('MDEntrySize'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            Int32NULL('NumberOfOrders'),
            uInt8('MDPriceLevel'),
            MDUpdateAction('MDUpdateAction'),
            MDEntryTypeBook('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class OrderIDEntriesPacket(Packet):
        name = 'OrderIDEntries'
        fields_desc = [
            uInt64('OrderID'),
            uInt64NULL('MDOrderPriority'),
            Int32NULL('MDDisplayQty'),
            uInt8NULL('ReferenceID'),
            OrderUpdateAction('OrderUpdateAction'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 32),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=32),
        PadField(LEShortField('OrderIDEntriesBlockSize', 24),align=7),
        FieldLenField('OrderIDEntriesCount', None, fmt='<B', count_of='OrderIDEntries'),
        PaddedPacketListField('OrderIDEntries',[],OrderIDEntriesPacket,count_from=lambda pkt: pkt.OrderIDEntriesCount,length_per_packet=24),
    ]
class MDIncrementalRefreshDailyStatistics(Packet):
    name = 'MDIncrementalRefreshDailyStatistics'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            PRICENULL9('MDEntryPx'),
            Int32NULL('MDEntrySize'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            LocalMktDate('TradingReferenceDate'),
            SettlPriceType('SettlPriceType'),
            MDUpdateAction('MDUpdateAction'),
            MDEntryTypeDailyStatistics('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 32),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=32),
    ]
class MDIncrementalRefreshLimitsBanding(Packet):
    name = 'MDIncrementalRefreshLimitsBanding'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            PRICENULL9('HighLimitPrice'),
            PRICENULL9('LowLimitPrice'),
            PRICENULL9('MaxPriceVariation'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            MDUpdateActionNew('MDUpdateAction'),
            MDEntryTypeLimits('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 32),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=32),
    ]
class MDIncrementalRefreshSessionStatistics(Packet):
    name = 'MDIncrementalRefreshSessionStatistics'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            PRICE9('MDEntryPx'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            OpenCloseSettlFlag('OpenCloseSettlFlag'),
            MDUpdateAction('MDUpdateAction'),
            MDEntryTypeStatistics('MDEntryType'),
            Int32NULL('MDEntrySize'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 24),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=24),
    ]
class MDIncrementalRefreshVolume(Packet):
    name = 'MDIncrementalRefreshVolume'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            Int32('MDEntrySize'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            MDUpdateAction('MDUpdateAction'),
            MDEntryTypeVol('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 16),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=16),
    ]
class SnapshotFullRefresh(Packet):
    name = 'SnapshotFullRefresh'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt32('LastMsgSeqNumProcessed'),
            uInt32('TotNumReports'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            uInt64('TransactTime'),
            uInt64('LastUpdateTime'),
            LocalMktDate('TradeDate'),
            SecurityTradingStatus('MDSecurityTradingStatus'),
            PRICENULL9('HighLimitPrice'),
            PRICENULL9('LowLimitPrice'),
            PRICENULL9('MaxPriceVariation'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=59)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            PRICENULL9('MDEntryPx'),
            Int32NULL('MDEntrySize'),
            Int32NULL('NumberOfOrders'),
            Int8NULL('MDPriceLevel'),
            LocalMktDate('TradingReferenceDate'),
            OpenCloseSettlFlag('OpenCloseSettlFlag'),
            SettlPriceType('SettlPriceType'),
            MDEntryType('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 22),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=22),
    ]
class QuoteRequest(Packet):
    name = 'QuoteRequest'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            QuoteReqId('QuoteReqID'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=35)
    
    class RelatedSymPacket(Packet):
        name = 'RelatedSym'
        fields_desc = [
            Symbol('Symbol'),
            Int32('SecurityID'),
            Int32NULL('OrderQty'),
            Int8('QuoteType'),
            Int8NULL('Side'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('RelatedSymBlockSize', 32),
        FieldLenField('RelatedSymCount', None, fmt='<B', count_of='RelatedSym'),
        PaddedPacketListField('RelatedSym',[],RelatedSymPacket,count_from=lambda pkt: pkt.RelatedSymCount,length_per_packet=32),
    ]
class MDInstrumentDefinitionOption(Packet):
    name = 'MDInstrumentDefinitionOption'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            MatchEventIndicator('MatchEventIndicator'),
            uInt32NULL('TotNumReports'),
            SecurityUpdateAction('SecurityUpdateAction'),
            uInt64('LastUpdateTime'),
            SecurityTradingStatus('MDSecurityTradingStatus'),
            Int16('ApplID'),
            uInt8('MarketSegmentID'),
            uInt8('UnderlyingProduct'),
            SecurityExchange('SecurityExchange'),
            SecurityGroup('SecurityGroup'),
            Asset('Asset'),
            Symbol('Symbol'),
            Int32('SecurityID'),
            SecurityIDSource('SecurityIDSource'),
            SecurityType('SecurityType'),
            CFICode('CFICode'),
            PutOrCall('PutOrCall'),
            MaturityMonthYear('MaturityMonthYear'),
            Currency('Currency'),
            PRICENULL9('StrikePrice'),
            Currency('StrikeCurrency'),
            Currency('SettlCurrency'),
            PRICENULL9('MinCabPrice'),
            CHAR('MatchAlgorithm'),
            uInt32('MinTradeVol'),
            uInt32('MaxTradeVol'),
            PRICENULL9('MinPriceIncrement'),
            PRICENULL9('MinPriceIncrementAmount'),
            Decimal9('DisplayFactor'),
            Int8NULL('TickRule'),
            uInt8NULL('MainFraction'),
            uInt8NULL('SubFraction'),
            uInt8NULL('PriceDisplayFormat'),
            UnitOfMeasure('UnitOfMeasure'),
            Decimal9NULL('UnitOfMeasureQty'),
            PRICENULL9('TradingReferencePrice'),
            SettlPriceType('SettlPriceType'),
            Int32NULL('ClearedVolume'),
            Int32NULL('OpenInterestQty'),
            PRICENULL9('LowLimitPrice'),
            PRICENULL9('HighLimitPrice'),
            UserDefinedInstrument('UserDefinedInstrument'),
            LocalMktDate('TradingReferenceDate'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=213)
    
    class EventsPacket(Packet):
        name = 'Events'
        fields_desc = [
            EventType('EventType'),
            uInt64('EventTime'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class MDFeedTypesPacket(Packet):
        name = 'MDFeedTypes'
        fields_desc = [
            MDFeedType('MDFeedType'),
            Int8('MarketDepth'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class InstAttribPacket(Packet):
        name = 'InstAttrib'
        fields_desc = [
            InstAttribType('InstAttribType'),
            InstAttribValue('InstAttribValue'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class LotTypeRulesPacket(Packet):
        name = 'LotTypeRules'
        fields_desc = [
            Int8('LotType'),
            DecimalQty('MinLotSize'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class UnderlyingsPacket(Packet):
        name = 'Underlyings'
        fields_desc = [
            Int32('UnderlyingSecurityID'),
            SecurityIDSource('UnderlyingSecurityIDSource'),
            UnderlyingSymbol('UnderlyingSymbol'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class RelatedInstrumentsPacket(Packet):
        name = 'RelatedInstruments'
        fields_desc = [
            Int32('RelatedSecurityID'),
            SecurityIDSource('RelatedSecurityIDSource'),
            Symbol('RelatedSymbol'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('EventsBlockSize', 9),
        FieldLenField('EventsCount', None, fmt='<B', count_of='Events'),
        PaddedPacketListField('Events',[],EventsPacket,count_from=lambda pkt: pkt.EventsCount,length_per_packet=9),
        LEShortField('MDFeedTypesBlockSize', 4),
        FieldLenField('MDFeedTypesCount', None, fmt='<B', count_of='MDFeedTypes'),
        PaddedPacketListField('MDFeedTypes',[],MDFeedTypesPacket,count_from=lambda pkt: pkt.MDFeedTypesCount,length_per_packet=4),
        LEShortField('InstAttribBlockSize', 4),
        FieldLenField('InstAttribCount', None, fmt='<B', count_of='InstAttrib'),
        PaddedPacketListField('InstAttrib',[],InstAttribPacket,count_from=lambda pkt: pkt.InstAttribCount,length_per_packet=4),
        LEShortField('LotTypeRulesBlockSize', 5),
        FieldLenField('LotTypeRulesCount', None, fmt='<B', count_of='LotTypeRules'),
        PaddedPacketListField('LotTypeRules',[],LotTypeRulesPacket,count_from=lambda pkt: pkt.LotTypeRulesCount,length_per_packet=5),
        LEShortField('UnderlyingsBlockSize', 24),
        FieldLenField('UnderlyingsCount', None, fmt='<B', count_of='Underlyings'),
        PaddedPacketListField('Underlyings',[],UnderlyingsPacket,count_from=lambda pkt: pkt.UnderlyingsCount,length_per_packet=24),
        LEShortField('RelatedInstrumentsBlockSize', 24),
        FieldLenField('RelatedInstrumentsCount', None, fmt='<B', count_of='RelatedInstruments'),
        PaddedPacketListField('RelatedInstruments',[],RelatedInstrumentsPacket,count_from=lambda pkt: pkt.RelatedInstrumentsCount,length_per_packet=24),
    ]
class MDIncrementalRefreshTradeSummary(Packet):
    name = 'MDIncrementalRefreshTradeSummary'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            PRICE9('MDEntryPx'),
            Int32('MDEntrySize'),
            Int32('SecurityID'),
            uInt32('RptSeq'),
            Int32('NumberOfOrders'),
            AggressorSide('AggressorSide'),
            MDUpdateAction('MDUpdateAction'),
            MDEntryTypeTrade('MDEntryType'),
            uInt32NULL('MDTradeEntryID'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    class OrderIDEntriesPacket(Packet):
        name = 'OrderIDEntries'
        fields_desc = [
            uInt64('OrderID'),
            Int32('LastQty'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 32),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=32),
        PadField(LEShortField('OrderIDEntriesBlockSize', 16),align=7),
        FieldLenField('OrderIDEntriesCount', None, fmt='<B', count_of='OrderIDEntries'),
        PaddedPacketListField('OrderIDEntries',[],OrderIDEntriesPacket,count_from=lambda pkt: pkt.OrderIDEntriesCount,length_per_packet=16),
    ]
class MDIncrementalRefreshOrderBook(Packet):
    name = 'MDIncrementalRefreshOrderBook'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt64('TransactTime'),
            MatchEventIndicator('MatchEventIndicator'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=11)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            uInt64NULL('OrderID'),
            uInt64NULL('MDOrderPriority'),
            PRICENULL9('MDEntryPx'),
            Int32NULL('MDDisplayQty'),
            Int32('SecurityID'),
            MDUpdateAction('MDUpdateAction'),
            MDEntryTypeBook('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 40),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=40),
    ]
class SnapshotFullRefreshOrderBook(Packet):
    name = 'SnapshotFullRefreshOrderBook'
    class FixBlock(Packet):
        name = 'FixBlock'
        fields_desc = [
            uInt32('LastMsgSeqNumProcessed'),
            uInt32('TotNumReports'),
            Int32('SecurityID'),
            uInt32('NoChunks'),
            uInt32('CurrentChunk'),
            uInt64('TransactTime'),
        ]
        def extract_padding(self, s):
            return '', s
            
    blockPadded = PadField(PacketField('block', default=FixBlock(),pkt_cls=FixBlock),align=28)
    
    class MDEntriesPacket(Packet):
        name = 'MDEntries'
        fields_desc = [
            uInt64('OrderID'),
            uInt64NULL('MDOrderPriority'),
            PRICE9('MDEntryPx'),
            Int32('MDDisplayQty'),
            MDEntryTypeBook('MDEntryType'),
        ]
        
        def extract_padding(self, s):
            return '', s
            
    fields_desc = [
        blockPadded,
        LEShortField('MDEntriesBlockSize', 29),
        FieldLenField('MDEntriesCount', None, fmt='<B', count_of='MDEntries'),
        PaddedPacketListField('MDEntries',[],MDEntriesPacket,count_from=lambda pkt: pkt.MDEntriesCount,length_per_packet=29),
    ]
packet_ids = { 
    4:dict(layer=ChannelReset,blockLength=9),
    12:dict(layer=AdminHeartbeat,blockLength=0),
    15:dict(layer=AdminLogin,blockLength=1),
    16:dict(layer=AdminLogout,blockLength=180),
    54:dict(layer=MDInstrumentDefinitionFuture,blockLength=216),
    56:dict(layer=MDInstrumentDefinitionSpread,blockLength=195),
    30:dict(layer=SecurityStatus,blockLength=30),
    46:dict(layer=MDIncrementalRefreshBook,blockLength=11),
    49:dict(layer=MDIncrementalRefreshDailyStatistics,blockLength=11),
    50:dict(layer=MDIncrementalRefreshLimitsBanding,blockLength=11),
    51:dict(layer=MDIncrementalRefreshSessionStatistics,blockLength=11),
    37:dict(layer=MDIncrementalRefreshVolume,blockLength=11),
    52:dict(layer=SnapshotFullRefresh,blockLength=59),
    39:dict(layer=QuoteRequest,blockLength=35),
    55:dict(layer=MDInstrumentDefinitionOption,blockLength=213),
    48:dict(layer=MDIncrementalRefreshTradeSummary,blockLength=11),
    47:dict(layer=MDIncrementalRefreshOrderBook,blockLength=11),
    53:dict(layer=SnapshotFullRefreshOrderBook,blockLength=28),
}
