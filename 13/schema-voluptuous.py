from voluptuous import Schema, Required, Length, All, Match, Optional, Coerce, Any

short_string = All(str, Length(1, 64))

schema = Schema({
    Required('firstname'): short_string,
    Required('lastname'): short_string,
    Optional('school', default=None): Any(None, {
        'name': str, 
        'address': {
            'street': str, 
            'number': All(Coerce(str), Match(r'^\d+[a-z]?'))
        }
    }),
    'modules': {
        Match(r'^[a-zA-Z0-9]+$'): {
            'name': str,
            'courses': [str]
        }
    },
    'grades': [float]
})