# Code Wars 7kyu - Find the Capitals

"""
Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.

The method should return an array of sentences declaring the state or country and its capital.

Examples
[{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
[{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
[{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]

"""

# My Solution
def capital(capitals): 
    sent = []
    for val in capitals:
        place = val['state'] if 'state' in val else val['country']
        sent.append(f"The capital of {place} is {val['capital']}")
    return sent

# One Liner

def capital(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]