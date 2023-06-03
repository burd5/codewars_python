"""
Regex Failure - Bug Fixing #2
Oh no, Timmy's received some hate mail recently but he knows better. Help Timmy 
fix his regex filter so he can be awesome again!

"""
# my solution

import re
def filter_words(phrase):
    return re.sub("(bad|mean|ugly|horrible|hideous)","awesome",phrase, flags=re.I)

# other solution using (?i)

from re import sub
def filter_words(phrase):
    return sub("(?i)(bad|mean|ugly|horrible|hideous)","awesome",phrase)