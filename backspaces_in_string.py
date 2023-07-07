# Backspaces in String - Codewars 6kyu

"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

"""

# My Solution

def clean_string(s):
    while "#" in s:
        index = s.find('#')
        if index == 0:
            s = s[1:]
        else:
            s = s[:index - 1] + s[index + 1:]
    return s

# Solution using Sub

import re

def clean_string(s):
  while '#' in s:
    s = re.sub('.?#', '', s, count=1)
  return s

