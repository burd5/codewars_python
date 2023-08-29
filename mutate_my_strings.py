# Mutate My Strings

"""
I will give you two strings. I want you to transform stringOne into stringTwo one letter at a time.

Example:

stringOne = 'bubble gum';
stringTwo = 'turtle ham';

Result:
bubble gum
tubble gum
turble gum
turtle gum
turtle hum
turtle ham

"""

def mutate_my_strings(s1, s2):
    res = [s1]
    s1 = list(s1)
    s2 = list(s2)
    for i, x in enumerate(s1):
        if s1[i] != s2[i]:
            s1[i] = s2[i]
            res.append(''.join(s1))
    return '\n'.join(res) + '\n'

def mutate_my_strings(s1,s2):
    s = s1 + '\n'
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        if s1[i] !=s2[i]:
            s1[i] = s2[i]
            s += "".join(s1) + '\n'
    return(s)

