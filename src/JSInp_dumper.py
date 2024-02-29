import json

class JSONDumper:
    def __init__(self, quantification_input):
        self.quantification_input = quantification_input

    def dump_to_json(self, file_path):
        # Convert QuantificationInput object to a dictionary
        quantification_input_dict = {
            'version': self.quantification_input.version,
            'saphiresolveinput': {
                'header': self._dump_header(self.quantification_input.saphiresolveinput['header']),
                'sysgatelist': [self._dump_sysgate(gate) for gate in self.quantification_input.saphiresolveinput['sysgatelist']],
                'faulttreelist': [self._dump_faulttree(tree) for tree in self.quantification_input.saphiresolveinput['faulttreelist']],
                'sequencelist': [self._dump_sequence(sequence) for sequence in self.quantification_input.saphiresolveinput['sequencelist']],
                'eventlist': [self._dump_event(event) for event in self.quantification_input.saphiresolveinput['eventlist']]
            }
        }

        # Dump the dictionary to a JSON file
        with open(file_path, 'w') as json_file:
            json.dump(quantification_input_dict, json_file, indent=4)

    def _dump_header(self, header):
        header_dict = {
            'projectpath': header.projectpath,
            'eventtree': header.eventtree.__dict__,
            'flagnum': header.flagnum,
            'ftcount': header.ftcount,
            'fthigh': header.fthigh,
            'sqcount': header.sqcount,
            'sqhigh': header.sqhigh,
            'becount': header.becount,
            'behigh': header.behigh,
            'mthigh': header.mthigh,
            'phhigh': header.phhigh,
            'truncparam': header.truncparam.__dict__,
            'workspacepair': header.workspacepair.__dict__,
            'iworkspacepair': header.iworkspacepair.__dict__
        }
        return header_dict

    def _dump_sysgate(self, gate):
        return gate.__dict__

    def _dump_faulttree(self, tree):
        fault_tree_dict = {
            'ftheader': tree.ftheader,
            'gatelist': [gate.__dict__ for gate in tree.gatelist]
        }
        return fault_tree_dict

    def _dump_sequence(self, sequence):
        return sequence.__dict__

    def _dump_event(self, event):
        return event.__dict__
