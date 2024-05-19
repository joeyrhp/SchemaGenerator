import json 

class SchemaStore:
    def __init__(self):
        self.schemas = {}

    def add_schema(self, schema):
        if schema._type in self.schemas:
            raise ValueError(f"Schema {schema._type} already exists")
        self.schemas[schema._type] = schema

    def get_schema(self, _type):
        return self.schemas.get(_type)

    def add_property_to_schema(self, _type, property):
        schema = self.get_schema(_type)
        if schema:
            schema.add_property(property)
        else:
            raise ValueError(f"Schema {_type} does not exist")
        
    def validate_schema_input(self, schema_type, json_payload):
        schema = self.get_schema(schema_type)
        if not schema:
            raise ValueError(f"Schema {schema_type} does not exist")

        try:
            json_data = json.loads(json_payload)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON payload")

        for property in schema.properties:
            if property.required and property.name not in json_data:
                raise ValueError(f"Missing required property {property.name}")

            if property.name in json_data:
                value = json_data[property.name]
                if property.type == "string" and not isinstance(value, str):
                    raise ValueError(f"Property {property.name} must be a string")
                elif property.type == "integer" and not isinstance(value, int):
                    raise ValueError(f"Property {property.name} must be an integer")
                # Add more type checks as needed

        return True