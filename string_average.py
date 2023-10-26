# String Average

"""
You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"

"""


# My Solution

def average_string(s):
    # dict for number string values
    dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    
    # counter to hold sum of values
    counter = 0
    
    # for loop to add together values
    for num in s.split():
        print(num)
        if num in dict:
            counter += dict[num]
        elif num not in dict:
            return 'n/a'
        
            
    # find floored average and return dict value that matches
    try:
        avg = counter//len(s.split())
    except:
        return 'n/a'
    
    key_values = list(dict.keys())
    dict_values = list(dict.values())
    
    position = dict_values.index(avg)
    
    return key_values[position]


# Other Solutions

N = ['zero','one','two','three','four','five','six','seven','eight','nine']

def average_string(s):
    try:
        return N[sum(N.index(w) for w in s.split()) // len(s.split())]
    except (ZeroDivisionError, ValueError):
        return 'n/a'
    
def average_string(s):
    if not s:
        return 'n/a'

    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    total = 0
    counter = 0
    for n in s.split():
        try:
            value = numbers.index(n)
            total += value
            counter += 1
        except:
            return 'n/a'
    return numbers[total // counter]