import json
from property import Property

class Schema:
    def __init__(self, json_string):
        valid, message = self.validate_input(json_string)
        if not valid:
            raise ValueError(message)

        data = json.loads(json_string)
        self._type = data['_type']
        self.properties = [property.Property(**property) for property in data['properties']]

    def add_property(self, property):
        self.properties.append(Property(**property))

    def __str__(self):
        return f'Schema: {self._type}\nProperties:\n' + '\n'.join([str(property) for property in self.properties])

    @staticmethod
    def validate_input(json_string):
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError:
            return False, "Invalid JSON"

        if '_type' not in data:
            return False, "Missing _type field"

        if 'properties' not in data:
            return False, "Missing properties field"

        if not isinstance(data['properties'], list):
            return False, "Properties must be a list"

        for property in data['properties']:
            if 'name' not in property:
                return False, "Property missing name field"
            if 'type' not in property:
                return False, "Property missing type field"
            if 'required' not in property:
                return False, "Property missing required field"

        return True, "Valid"