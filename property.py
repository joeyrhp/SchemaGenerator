class Property:
    def __init__(self, name, type, required):
        self.name = name
        self.type = type
        self.required = required

    def __str__(self):
        return f'Property: {self.name}, Type: {self.type}, Required: {self.required}'