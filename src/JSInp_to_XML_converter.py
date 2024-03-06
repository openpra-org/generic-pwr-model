from opsa_mef import ModelData
import xml.etree.ElementTree as ET

class JSONtoXMLConverter:
    def __init__(self, parsed_json_object):
        self.parsed_json_object = parsed_json_object

    def convert_to_xml(self):
        model_data = self._convert_eventlist_to_modeldata()
        return model_data.to_xml()
        # return ET.tostring(model_data.to_xml(), encoding='unicode')  # Serialize the XML element to string

    def _convert_eventlist_to_modeldata(self):
        model_data = ModelData()

        # Accessing eventlist attribute directly from parsed JSON object
        eventlist = self.parsed_json_object.saphiresolveinput.get('eventlist', [])

        for event in eventlist:
            name = event.id
            label = event.name
            value = event.value

            # Skip certain labels
            if label in ['<TRUE>', '<FALSE>', '<PASS>']:
                continue

            # Add basic event to model data
            model_data.add_basic_event(name, label=label, float_value=value)

        return model_data
