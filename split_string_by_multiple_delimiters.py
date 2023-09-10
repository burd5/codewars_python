# Split String By Multiple Delimiters

"""
import re
def multiple_split(string, delimiters=[]):
return [x for x in re.split('|'.join(map(re.escape, delimiters)), string) if x != '']

"""

import re
def multiple_split(string, delimiters=[]):
	return [x for x in re.split('|'.join(map(re.escape, delimiters)), string) if x != '']