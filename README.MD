# Project Documentation

## Overview

This project is a Python-based schema validation system. It allows users to define schemas using a JSON-based format and then validate JSON payloads against those schemas.

## Schema Format

Schemas are defined using a JSON object with the following structure:

- **_type**: The type of the schema.
- **properties**: A list of properties, where each property is an object with the following keys:
  - **name**: The name of the property.
  - **type**: The type of the property (e.g. "string", "integer").
  - **required**: A boolean indicating whether the property is required or not.

### Example Schema

```json
{
  "_type": "Person",
  "properties": [
    {"name": "name", "type": "string", "required": true},
    {"name": "age", "type": "integer", "required": false}
  ]
}
```

## Class Documentation

### Property Class

- `__init__(self, name, type, required)`: Initializes a new Property object.
  - **name**: The name of the property.
  - **type**: The type of the property.
  - **required**: A boolean indicating whether the property is required or not.

### Schema Class

- `__init__(self, json_string)`: Initializes a new Schema object from a JSON string.
- `validate_schema_input(self, json_payload)`: Validates a JSON payload against the schema.
- `add_property(self, property)`: Adds a new property to the schema.

### SchemaStore Class

- `__init__(self)`: Initializes a new SchemaStore object.
- `add_schema(self, schema)`: Adds a new schema to the store.
- `get_schema(self, schema_type)`: Retrieves a schema from the store by its type.
- `validate_schema_input(self, schema_type, json_payload)`: Validates a JSON payload against a schema in the store.

## Testing

To test the code, you can use the following example:

```python
import json

# Create a schema
json_string = '''
{
    "_type": "Person",
    "properties": [
        {"name": "name", "type": "string", "required": true},
        {"name": "age", "type": "integer", "required": false}
    ]
}
'''

schema = Schema(json_string)

# Create a schema store
schema_store = SchemaStore()
schema_store.add_schema(schema)

# Validate a JSON payload
json_payload = '''
{
    "name": "John Doe",
    "age": 30
}
'''

if schema_store.validate_schema_input("Person", json_payload):
    print("Input is valid")
else:
    print("Input is invalid")
```

## Execution

To execute the code, simply run the Python script containing the code. You can also use the `SchemaStore` class to add schemas and validate JSON payloads programmatically.

## Troubleshooting

- Make sure that the JSON payload is well-formed and matches the schema definition.
- Check that the schema is correctly added to the `SchemaStore` instance.
- Verify that the `validate_schema_input` method is called with the correct schema type and JSON payload.