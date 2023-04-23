"""
DropCaps means that the first letter of the starting word of the paragraph 
should be in caps and the remaining lowercase, just like you see in the newspaper.

But for a change, let"s do that for each and every word of the given String. 
Your task is to capitalize every word that has length greater than 2, leaving 
smaller words as they are.

*should work also on Leading and Trailing Spaces and caps.

"apple"            => "Apple"
"apple of banana"  => "Apple of Banana"
"one   space"      => "One   Space 
"   space WALK   " => "   Space Walk   " 

"""

import re
def drop_cap(str_):
    new_str = ''
    str = re.split(r'(\s+)', str_)
    for word in str:
        if len(word) > 2:
            new_str += word.title()
        else:
            new_str += word
            
    return new_str

# other solution

def drop_cap(str_):
    return ' '.join( w.capitalize() if len(w) > 2 else w for w in str_.split(' ') )