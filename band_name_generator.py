"""

My friend wants a new band name for her band. She like bands that use the formula: "The" + a noun with the first letter capitalized, for example:

"dolphin" -> "The Dolphin"

However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice and connect them together with the first and last letter, combined into one word (WITHOUT "The" in front), like this:

"alaska" -> "Alaskalaska"

Complete the function that takes a noun as a string, and returns her preferred band name written as a string.

"""

# my solution

def band_name_generator(name):
    if name[0] == name[-1]:
        return name[0].upper() + name[1:-1] + name.lower()
    else:
        return "The " + name[0].upper() + name[1:]
    
# more concise ways using capitalize and title

def band_name_generator(name):
    return name.capitalize()+name[1:] if name[0]==name[-1] else 'The '+ name.capitalize()

def band_name_generator(name):
    if name[0] == name[-1]:
        return name.title()+name[1:]
    return ("the "+name).title()