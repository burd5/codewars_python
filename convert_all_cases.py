# Convert All Cases

"""
In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.

You must write a function that changes to a given case. It must be able to handle all three case types:

py> change_case("snakeCase", "snake")
"snake_case"
py> change_case("some-lisp-name", "camel")
"someLispName"
py> change_case("map_to_all", "kebab")
"map-to-all"
py> change_case("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
py> change_case("invalid-inPut_bad", "kebab")
None
py> change_case("valid-input", "huh???")
None
py> change_case("", "camel")
""
Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase.

"""

import re

def change_case(label, target):
    if ('_' in label) + ('-' in label) + (label != label.lower()) > 1:
        return
    
    if target == 'snake':
        return re.sub('([A-Z])', r'_\1', label.replace('-', '_')).lower()
    
    if target == 'kebab':
        return re.sub('([A-Z])', r'-\1', label.replace('_', '-')).lower()
    
    if target == 'camel':
        return re.sub('([_-])([a-z])', lambda m: m.group(2).upper(), label)

def change_case(label, case):
    if case not in ['snake', 'kebab', 'camel'] or ('_' in label) + ('-' in label) + (label != label.lower()) > 1:
        return
    
    return ''.join( '_' + c.lower() if c.isupper()  and case == 'snake' else
                    '_' if c == '-'                 and case == 'snake' else
                    
                    '-' + c.lower() if c.isupper()  and case == 'kebab' else
                    '-' if c == '_'                 and case == 'kebab' else
                    
                    c.upper() if label[i-1] in '-_' and case == 'camel' else
                    '' if c in '-_'                 and case == 'camel' else
                    
                    c for i, c in enumerate(label) )