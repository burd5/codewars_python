"""
You must create a method that can convert a string from any format into PascalCase. This must support symbols too.

Don't presume the separators too much or you could be surprised.

For example: (Input --> Output)

"example name" --> "ExampleName"
"your-NaMe-here" --> "YourNameHere"
"testing ABC" --> "TestingAbc"

"""

# my solution

from re import split

def camelize(string):
    return ''.join(x.capitalize() for x in split('([^a-zA-Z0-9])', string)
                   if x.isalnum())

# solution I was going for

import re

def camelize(s):
    return "".join([w.capitalize() for w in re.split("\W|_", s)])