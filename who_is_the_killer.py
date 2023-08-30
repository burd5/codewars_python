# Who is the Killer

"""
Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
and also a list of the names of the dead people:

['Lucas', 'Bill']
return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

"""
# My solution

def killer(suspect_info, dead):
    return [key for key,val in suspect_info.items() if all(x in val for x in dead)][0]

# Other Solutions

def killer(suspect_info, dead):
    for x in suspect_info:
        if all(people in suspect_info[x] for people in dead):
            return x
        
def killer(info, dead):
    for name, seen in info.items():
        if set(dead) <= set(seen):
            return name