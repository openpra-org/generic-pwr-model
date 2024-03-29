import json

class EventTree:
    def __init__(self, name, number, initevent, seqphase):
        self.name = name
        self.number = number
        self.initevent = initevent
        self.seqphase = seqphase

class TruncParam:
    def __init__(self, ettruncopt, fttruncopt, sizeopt, ettruncval, fttruncval, sizeval, transrepl, transzones, translevel, usedual, dualcutoff):
        self.ettruncopt = ettruncopt
        self.fttruncopt = fttruncopt
        self.sizeopt = sizeopt
        self.ettruncval = ettruncval
        self.fttruncval = fttruncval
        self.sizeval = sizeval
        self.transrepl = transrepl
        self.transzones = transzones
        self.translevel = translevel
        self.usedual = usedual
        self.dualcutoff = dualcutoff

class WorkspacePair:
    def __init__(self, ph, mt):
        self.ph = ph
        self.mt = mt

class Header:
    def __init__(self, projectpath, eventtree, flagnum, ftcount, fthigh, sqcount, sqhigh, becount, behigh, mthigh, phhigh, truncparam, workspacepair, iworkspacepair):
        self.projectpath = projectpath
        self.eventtree = eventtree
        self.flagnum = flagnum
        self.ftcount = ftcount
        self.fthigh = fthigh
        self.sqcount = sqcount
        self.sqhigh = sqhigh
        self.becount = becount
        self.behigh = behigh
        self.mthigh = mthigh
        self.phhigh = phhigh
        self.truncparam = truncparam
        self.workspacepair = workspacepair
        self.iworkspacepair = iworkspacepair

class SysGate:
    def __init__(self, name, id, gateid, gateorig, gatepos, eventid, gatecomp, comppos, compflag, gateflag, gatet, bddsuccess, done):
        self.name = name
        self.id = id
        self.gateid = gateid
        self.gateorig = gateorig
        self.gatepos = gatepos
        self.eventid = eventid
        self.gatecomp = gatecomp
        self.comppos = comppos
        self.compflag = compflag
        self.gateflag = gateflag
        self.gatet = gatet
        self.bddsuccess = bddsuccess
        self.done = done

class FaultTree:
    def __init__(self, ftheader, gatelist):
        self.ftheader = ftheader
        self.gatelist = gatelist

class Gate:
    def __init__(self, gateid, gatetype, numinputs, gateinput=None, eventinput=None, compeventinput=None):
        self.gateid = gateid
        self.gatetype = gatetype
        self.numinputs = numinputs
        self.gateinput = gateinput
        self.eventinput = eventinput
        self.compeventinput = compeventinput

class Sequence:
    def __init__(self, seqid, etid, initid, qmethod, qpasses, numlogic, blocksize, logiclist):
        self.seqid = seqid
        self.etid = etid
        self.initid = initid
        self.qmethod = qmethod
        self.qpasses = qpasses
        self.numlogic = numlogic
        self.blocksize = blocksize
        self.logiclist = logiclist

class Event:
    def __init__(self, id, corrgate, name, evworkspacepair, value, initf, processf, calctype):
        self.id = id
        self.corrgate = corrgate
        self.name = name
        self.evworkspacepair = evworkspacepair
        self.value = value
        self.initf = initf
        self.processf = processf
        self.calctype = calctype

class JSInp:
    def __init__(self, version, saphiresolveinput):
        self.version = version
        self.saphiresolveinput = saphiresolveinput

class JSONParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.parse_from_json()

    def parse_from_json(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def parse_to_object(self):
        saphsolve_input = self.data

        # Parse the 'header' section
        header_data = saphsolve_input['saphiresolveinput']['header']
        header = Header(
            projectpath=header_data['projectpath'],
            eventtree=EventTree(**header_data['eventtree']),
            flagnum=header_data['flagnum'],
            ftcount=header_data['ftcount'],
            fthigh=header_data['fthigh'],
            sqcount=header_data['sqcount'],
            sqhigh=header_data['sqhigh'],
            becount=header_data['becount'],
            behigh=header_data['behigh'],
            mthigh=header_data['mthigh'],
            phhigh=header_data['phhigh'],
            truncparam=TruncParam(**header_data['truncparam']),
            workspacepair=WorkspacePair(**header_data['workspacepair']),
            iworkspacepair=WorkspacePair(**header_data['iworkspacepair'])
        )

        # Parse the 'sysgatelist' section
        sysgatelist_data = saphsolve_input['saphiresolveinput']['sysgatelist']
        sysgatelist = [SysGate(**gate_data) for gate_data in sysgatelist_data]

        # # Parse the 'faulttreelist' section
        # faulttreelist_data = saphsolve_input['saphiresolveinput']['faulttreelist']
        # faulttreelist = [FaultTree(
        #     ftheader=fault['ftheader'],
        #     gatelist=[Gate(**gate_data) for gate_data in fault['gatelist']]
        # ) for fault in faulttreelist_data]

        # Parse the 'faulttreelist' section
        faulttreelist_data = saphsolve_input['saphiresolveinput']['faulttreelist']
        faulttreelist = []
        for fault in faulttreelist_data:
            if 'gatelist' in fault:
                gatelist = [Gate(**gate_data) for gate_data in fault['gatelist']]
            else:
                gatelist = None  # or any other appropriate value to represent absence of gatelist
            fault_tree = FaultTree(
                ftheader=fault['ftheader'],
                gatelist=gatelist
            )
            faulttreelist.append(fault_tree)

        # Parse the 'sequencelist' section if it exists
        if 'sequencelist' in saphsolve_input['saphiresolveinput']:
            sequencelist_data = saphsolve_input['saphiresolveinput']['sequencelist']
            sequencelist = [Sequence(**sequence_data) for sequence_data in sequencelist_data]
        else:
            sequencelist = []

        # Parse the 'eventlist' section
        eventlist_data = saphsolve_input['saphiresolveinput']['eventlist']
        eventlist = [Event(**event_data) for event_data in eventlist_data]

        # Create the QuantificationInput object
        saphsolve_input_object = JSInp(
            version=saphsolve_input['version'],
            saphiresolveinput={
                'header': header,
                'sysgatelist': sysgatelist,
                'faulttreelist': faulttreelist,
                'sequencelist': sequencelist,
                'eventlist': eventlist
            }
        )

        return saphsolve_input_object
