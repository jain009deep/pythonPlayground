
from datetime import datetime
from threading import Timer


xmlString = """<?xml version="1.0" encoding="UTF-8"?>
<ns0:FlightEvent xmlns:ns0="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flightevent">
    <ns0:EventHeader>
        <ns1:EventDomain xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">Flight</ns1:EventDomain>
        <ns1:EventType xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">Flight</ns1:EventType>
        <ns1:EventSubType xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">OutTime</ns1:EventSubType>
        <ns1:EventVersion xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">1.0</ns1:EventVersion>
        <ns1:EventId xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">20151009134058057.B6034120151010STX10.3</ns1:EventId>
        <ns1:EventCreationSystem xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">FPES</ns1:EventCreationSystem>
        <ns1:EventCreationSystemId xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">EventProcessor</ns1:EventCreationSystemId>
        <ns1:EventCreationHost xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">FPESEventProcessor-Flight-FPESEventProcessorArchive</ns1:EventCreationHost>
        <ns1:EventCreatingProcessId xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">FPESEventProcessor-Flight-FPESEventProcessorArchive</ns1:EventCreatingProcessId>
        <ns1:EventCorrelationId xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">151009174036.02</ns1:EventCorrelationId>
        <ns1:EventCreationDateTime xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">2015-10-09T13:40:58.057-04:00</ns1:EventCreationDateTime>
        <ns1:EntitySeqNumber xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">3</ns1:EntitySeqNumber>
        <ns1:EntityUTCUpdateTimeStamp xmlns:ns1="http://www.schemas.jetblue.com/2013/12/enterprise/eventheader">1444412458057</ns1:EntityUTCUpdateTimeStamp>
    </ns0:EventHeader>
    <ns0:ChangedFlightLeg>
        <ns0:SchFlightLegKey>B6034120151010STX</ns0:SchFlightLegKey>
        <ns0:ActFlightLegKey>B6034120151010STX10</ns0:ActFlightLegKey>
        <ns0:ChangedFlightLegElements>
            <ns0:ElementXPath>B6034120151010STX:Status</ns0:ElementXPath>
            <ns0:ElementXPath>B6034120151010STX10: ActLocalOutDateTime, SourceMessageDateTime, SourceMessageType, SourceUpdateDateTime, SourceSystemName, EventCorrelationId,DepProgress, LegStatus</ns0:ElementXPath>
        </ns0:ChangedFlightLegElements>
    </ns0:ChangedFlightLeg>
    <ns0:Flight>
        <ns1:FlightKey xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">B6034120151010</ns1:FlightKey>
        <ns1:FlightCarrierCode xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">B6</ns1:FlightCarrierCode>
        <ns1:FlightNumber xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">0341</ns1:FlightNumber>
        <ns1:FlightOriginLocalDate xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">2015-10-10</ns1:FlightOriginLocalDate>
        <ns1:FlightOriginStnCode xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">STX</ns1:FlightOriginStnCode>
        <ns1:FlightDestStnCode xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">SJU</ns1:FlightDestStnCode>
        <ns1:EntitySeqNumber xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">3</ns1:EntitySeqNumber>
        <ns1:EntityUTCUpdateTimeStamp xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">1443852009177</ns1:EntityUTCUpdateTimeStamp>
        <ns1:ScheduledFlightLeg xmlns:ns1="http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight">
            <ns1:SchFlightLegKey>B6034120151010STX</ns1:SchFlightLegKey>
            <ns1:FlightCarrierCode>B6</ns1:FlightCarrierCode>
            <ns1:FlightNumber>0341</ns1:FlightNumber>
            <ns1:SchLocalDepDate>2015-10-10</ns1:SchLocalDepDate>
            <ns1:SchDepStnCode>STX</ns1:SchDepStnCode>
            <ns1:FlightOriginLocalDate>2015-10-10</ns1:FlightOriginLocalDate>
            <ns1:FlightLegSeqNumber>10</ns1:FlightLegSeqNumber>
            <ns1:ServiceType>J</ns1:ServiceType>
            <ns1:FlightType>SCH</ns1:FlightType>
            <ns1:Status>TAXIING</ns1:Status>
            <ns1:SchLocalDepDateTime>2015-10-10T15:38:00-04:00</ns1:SchLocalDepDateTime>
            <ns1:SchArrStnCode>SJU</ns1:SchArrStnCode>
            <ns1:SchLocalArrDateTime>2015-10-10T16:18:00-04:00</ns1:SchLocalArrDateTime>
            <ns1:ArrTerminal>A</ns1:ArrTerminal>
            <ns1:OnTimePerfValue>8</ns1:OnTimePerfValue>
            <ns1:OnTimePerfPeriod>AUG15</ns1:OnTimePerfPeriod>
            <ns1:SecureFlightIndicator>true</ns1:SecureFlightIndicator>
            <ns1:SchAcftOwner>B6</ns1:SchAcftOwner>
            <ns1:EqpmtType>E90</ns1:EqpmtType>
            <ns1:SchAcftConfig>Y100                </ns1:SchAcftConfig>
            <ns1:SchOnwardFlightNumber>2037</ns1:SchOnwardFlightNumber>
            <ns1:SchOnwardFlightCarrierCode>B6</ns1:SchOnwardFlightCarrierCode>
            <ns1:SourceSystemName>SchedMgr</ns1:SourceSystemName>
            <ns1:SourceMessageType>SCH</ns1:SourceMessageType>
            <ns1:SourceUpdateDateTime>2015-10-03T02:00:00Z</ns1:SourceUpdateDateTime>
            <ns1:MarketingFlightSegment>
                <ns1:MarketingFlightSegKey>B6034120151010STXSJU</ns1:MarketingFlightSegKey>
                <ns1:MarketingCarrierCode>B6</ns1:MarketingCarrierCode>
                <ns1:MarketingFlightNumber>0341</ns1:MarketingFlightNumber>
                <ns1:FlightSegOriginAirport>STX</ns1:FlightSegOriginAirport>
                <ns1:FlightSegDestAirport>SJU</ns1:FlightSegDestAirport>
                <ns1:FlightSegOriginLocalDate>2015-10-10</ns1:FlightSegOriginLocalDate>
                <ns1:FlightSegOriginLocalDateTime>2015-10-10T15:38:00-04:00</ns1:FlightSegOriginLocalDateTime>
                <ns1:FlightSegDestLocalDateTime>2015-10-10T16:18:00-04:00</ns1:FlightSegDestLocalDateTime>
                <ns1:SourceSystemName>SchedMgr</ns1:SourceSystemName>
                <ns1:SourceMessageType>SCH</ns1:SourceMessageType>
                <ns1:SourceUpdateDateTime>2015-10-03T02:00:00Z</ns1:SourceUpdateDateTime>
            </ns1:MarketingFlightSegment>
            <ns1:ActualFlightLeg>
                <ns1:ActFlightLegKey>B6034120151010STX10</ns1:ActFlightLegKey>
                <ns1:FlightCarrierCode>B6</ns1:FlightCarrierCode>
                <ns1:FlightNumber>0341</ns1:FlightNumber>
                <ns1:LocalDepDate>2015-10-10</ns1:LocalDepDate>
                <ns1:DepStnCode>STX</ns1:DepStnCode>
                <ns1:SourceFlightLegSeqNumber>10</ns1:SourceFlightLegSeqNumber>
                <ns1:ActFlightLegSeqNumber>1</ns1:ActFlightLegSeqNumber>
                <ns1:LegStatus>TAXIING</ns1:LegStatus>
                <ns1:ServiceType>J</ns1:ServiceType>
                <ns1:ActFlightType>SCH</ns1:ActFlightType>
                <ns1:SchFlightType>SCH</ns1:SchFlightType>
                <ns1:LocalDepDateTime>2015-10-10T15:38:00-04:00</ns1:LocalDepDateTime>
                <ns1:ArrStnCode>SJU</ns1:ArrStnCode>
                <ns1:LocalArrDateTime>2015-10-10T16:18:00-04:00</ns1:LocalArrDateTime>
                <ns1:EstLocalPubDepDateTime>2015-10-10T15:38:00-04:00</ns1:EstLocalPubDepDateTime>
                <ns1:EstLocalPubArrDateTime>2015-10-10T16:22:00-04:00</ns1:EstLocalPubArrDateTime>
                <ns1:ActLocalOutDateTime>2015-10-10T15:42:00-04:00</ns1:ActLocalOutDateTime>
                <ns1:EqpmtType>E90</ns1:EqpmtType>
                <ns1:AcftRegNumber>N193JB</ns1:AcftRegNumber>
                <ns1:ReplacedFromSourceFlightLegSeqNumber>0</ns1:ReplacedFromSourceFlightLegSeqNumber>
                <ns1:ArrProgress>E</ns1:ArrProgress>
                <ns1:DepProgress>A</ns1:DepProgress>
                <ns1:ATCStatus>0</ns1:ATCStatus>
                <ns1:FITIndicator>false</ns1:FITIndicator>
                <ns1:SourceFlightLegId>0003614477</ns1:SourceFlightLegId>
                <ns1:EventCorrelationId>151009174036.02</ns1:EventCorrelationId>
                <ns1:SourceSystemName>FliteTrac</ns1:SourceSystemName>
                <ns1:DispatchDeskId>DM</ns1:DispatchDeskId>
                <ns1:SourceUpdateUserId>AVEJ</ns1:SourceUpdateUserId>
                <ns1:SourceMessageType>OUT</ns1:SourceMessageType>
                <ns1:SourceMessageDateTime>2015-10-09T17:40:35Z</ns1:SourceMessageDateTime>
                <ns1:SourceUpdateDateTime>2015-10-09T17:40:00Z</ns1:SourceUpdateDateTime>
                <ns1:FlightLegReason>
                    <ns1:ReasonCategory>DELAY</ns1:ReasonCategory>
                    <ns1:ReasonType>ESTIMATED</ns1:ReasonType>
                    <ns1:ReasonSubType>5</ns1:ReasonSubType>
                    <ns1:DelayReasonMinutes>4</ns1:DelayReasonMinutes>
                    <ns1:DelayUpdateDateTime>2015-10-09T17:40:35Z</ns1:DelayUpdateDateTime>
                </ns1:FlightLegReason>
                <ns1:ActFlightLegKey>B6034120151010STX10</ns1:ActFlightLegKey>
                <ns1:FlightCarrierCode>B6</ns1:FlightCarrierCode>
                <ns1:FlightNumber>0341</ns1:FlightNumber>
                <ns1:LocalDepDate>2015-10-10</ns1:LocalDepDate>
                <ns1:DepStnCode>STX</ns1:DepStnCode>
                <ns1:SourceFlightLegSeqNumber>10</ns1:SourceFlightLegSeqNumber>
                <ns1:ActFlightLegSeqNumber>1</ns1:ActFlightLegSeqNumber>
                <ns1:LegStatus>TAXIING</ns1:LegStatus>
                <ns1:ServiceType>J</ns1:ServiceType>
                <ns1:ActFlightType>SCH</ns1:ActFlightType>
                <ns1:SchFlightType>SCH</ns1:SchFlightType>
                <ns1:LocalDepDateTime>2015-10-10T15:38:00-04:00</ns1:LocalDepDateTime>
                <ns1:ArrStnCode>SJU</ns1:ArrStnCode>
                <ns1:LocalArrDateTime>2015-10-10T16:18:00-04:00</ns1:LocalArrDateTime>
                <ns1:EstLocalPubDepDateTime>2015-10-10T15:38:00-04:00</ns1:EstLocalPubDepDateTime>
                <ns1:EstLocalPubArrDateTime>2015-10-10T16:22:00-04:00</ns1:EstLocalPubArrDateTime>
                <ns1:ActLocalOutDateTime>2015-10-10T15:42:00-04:00</ns1:ActLocalOutDateTime>
                <ns1:EqpmtType>E90</ns1:EqpmtType>
                <ns1:AcftRegNumber>N193JB</ns1:AcftRegNumber>
                <ns1:ReplacedFromSourceFlightLegSeqNumber>0</ns1:ReplacedFromSourceFlightLegSeqNumber>
                <ns1:ArrProgress>E</ns1:ArrProgress>
                <ns1:DepProgress>A</ns1:DepProgress>
                <ns1:ATCStatus>0</ns1:ATCStatus>
                <ns1:FITIndicator>false</ns1:FITIndicator>
                <ns1:SourceFlightLegId>0003614477</ns1:SourceFlightLegId>
                <ns1:EventCorrelationId>151009174036.02</ns1:EventCorrelationId>
                <ns1:SourceSystemName>FliteTrac</ns1:SourceSystemName>
                <ns1:DispatchDeskId>DM</ns1:DispatchDeskId>
                <ns1:SourceUpdateUserId>AVEJ</ns1:SourceUpdateUserId>
                <ns1:SourceMessageType>OUT</ns1:SourceMessageType>
                <ns1:SourceMessageDateTime>2015-10-09T17:40:35Z</ns1:SourceMessageDateTime>
                <ns1:SourceUpdateDateTime>2015-10-09T17:40:00Z</ns1:SourceUpdateDateTime>
                <ns1:FlightLegReason>
                    <ns1:ReasonCategory>DELAY</ns1:ReasonCategory>
                    <ns1:ReasonType>ESTIMATED</ns1:ReasonType>
                    <ns1:ReasonSubType>5</ns1:ReasonSubType>
                    <ns1:DelayReasonMinutes>4</ns1:DelayReasonMinutes>
                    <ns1:DelayUpdateDateTime>2015-10-09T17:40:35Z</ns1:DelayUpdateDateTime>
                </ns1:FlightLegReason>
            </ns1:ActualFlightLeg>
        </ns1:ScheduledFlightLeg>
    </ns0:Flight>
</ns0:FlightEvent>"""
class D0:
    delayedCount = 0
    totalCount = 0
    def __init__(self):
        type(self).delayedCount = 0 
        type(self).totalCount = 0 
        Timer(600, self.__init__).start()
        
    
    def getDepVariance(self, xmlString):
        import xmltodict
        from dateutil.parser import parse
        doc = xmltodict.parse(xmlString.strip(), process_namespaces=True, namespaces={'http://www.schemas.jetblue.com/2015/06/enterprise/flight/flightevent':None, 'http://www.schemas.jetblue.com/2013/12/enterprise/eventheader':None, 'http://www.schemas.jetblue.com/2015/06/enterprise/flight/flight':None})
    # XMLSTRING.strip(), process_namespaces=True, namespaces={'C':None, 'xsi':None, 'http://www.w3.org/2001/XMLSchema-instance':None}
    
        schLocalDepDateTime = doc["FlightEvent"]["Flight"]['ScheduledFlightLeg']['SchLocalDepDateTime'];
        actLocalOutDateTime = doc["FlightEvent"]["Flight"]['ScheduledFlightLeg']['ActualFlightLeg']['ActLocalOutDateTime'][0];
    
        d =  (parse(actLocalOutDateTime)-  parse(schLocalDepDateTime)).seconds/60
    
        #doc["FlightEvent"]["Flight"]['ScheduledFlightLeg']['SchLocalDepDateTime']
        return d
    
    def calculateD0(self, xmlString):
        type(self).totalCount += 1
        depVariance = self.getDepVariance(xmlString)
        if depVariance > 0 :
             type(self).delayedCount += 1
        print "D0 t"+str( type(self).totalCount)
        print "D0 d"+str( type(self).delayedCount)
        return  type(self).delayedCount/ type(self).totalCount
        
#     def resetCount(self):
        
        
# x=datetime.today()
# y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
# delta_t=y-x
# 
# secs=delta_t.seconds+1

def hello_world():
    print "hello world"
    Timer(10, hello_world).start()
    #...

# hello_world()
# d0 = D0();
# d0_val = d0.calculateD0(xmlString)
# print d0_val 
