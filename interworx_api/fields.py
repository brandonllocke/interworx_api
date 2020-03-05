class Fields:
    def __init__(self, possible_fields, **provided_fields):
        self.required = possible_fields.get('required', {})
        self.optional = possible_fields.get('optional', {})
        self.possible = {**self.required, **self.optional}
        self.provided = provided_fields

    def check_required_fields(self):
        try:
            for field in self.required:
                assert field in self.provided
        except AssertionError:
            print(f'Query is missing the required "{field}" parameter.')
            return False
        return True
    
    def validate_fields(self):
        for field in self.provided:
            try:
                field = Field(self.provided[field], self.possible[field])
                field.validate()
            except KeyError:
                print(f'The provided parameter "{field}" is unknown and will be ignored.')
                return False
        return True

        
class Field:
    def __init__(self, var, exp_type):
        self.var = var
        self.exp_type = exp_type

    def validate(self):
        try:
            self.exp_type(self.var)
        except (ValueError, TypeError):
            print(f'Could not validate {self.var} as {self.exp_type}. Query not sent.')