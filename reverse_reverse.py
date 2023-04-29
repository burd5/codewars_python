"""
In this kata you must take an input string, reverse the order of the words, and
reverse the order of the letters within the words.

But, as a bonus, every test input will end with a punctuation mark (! ? .) and 
the output should be returned with the mark at the end.

A few examples should help clarify:

esrever("hello world.") == "dlrow olleh."

esrever("Much l33t?") == "t33l hcuM?"

esrever("tacocat!") == "tacocat!"

"""

# my solution

def esrever(string):
    new_str = ''
    for letter in reversed(string):
        new_str += letter
        
    return '' if string == '' else new_str[1:] + string[-1]

# one line solution

def esrever(s):
    return s[:-1][::-1] + s[-1] if s else ''