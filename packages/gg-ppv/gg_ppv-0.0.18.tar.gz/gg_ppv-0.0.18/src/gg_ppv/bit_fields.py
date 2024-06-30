from scapy.fields import *
from scapy.volatile import RandNum

class PaddedFlagsField(FlagsField):
    def randval(self):
        return RandNum(0, 2**len(self.names)-1)
InstAttribValue = lambda name: PaddedFlagsField(name, 0, 32, ['ElectronicMatchEligible', 'OrderCrossEligible', 'BlockTradeEligible', 'EFPEligible', 'EBFEligible', 'EFSEligible', 'EFREligible', 'OTCEligible', 'iLinkIndicativeMassQuotingEligible', 'NegativeStrikeEligible', 'NegativePriceOutrightEligible', 'IsFractional', 'VolatilityQuotedOption', 'RFQCrossEligible', 'ZeroPriceOutrightEligible', 'DecayingProductEligibility', 'VariableProductEligibility', 'DailyProductEligibility', 'GTOrdersEligibility', 'ImpliedMatchingEligibility', 'TriangulationEligible', 'VariableCabEligible'])
MatchEventIndicator = lambda name: PaddedFlagsField(name, 0, 8, ['LastTradeMsg', 'LastVolumeMsg', 'LastQuoteMsg', 'LastStatsMsg', 'LastImpliedMsg', 'RecoveryMsg', 'Reserved', 'EndOfEvent'])
SettlPriceType = lambda name: PaddedFlagsField(name, 0, 8, ['FinalDaily', 'Actual', 'Rounded', 'Intraday', 'ReservedBits', 'NullValue'])
