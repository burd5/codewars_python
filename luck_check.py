# Luck Check

"""
003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6

"""

# My Solution

def luck_check(string):
    mid = len(string) // 2
    
    if not string.isnumeric(): raise Error

    if len(string) % 2 == 0:
        first = sum([int(x) for x in string[:mid]])
        second = sum([int(x) for x in string[mid:]])
        return first == second
    else:
        first = sum([int(x) for x in string[:mid]])
        second = sum([int(x) for x in string[mid + 1:]])
        print(first, second)
        return first == second
    
# Other Solution

def luck_check(s):
    if not s.isnumeric(): raise ValueError
    return not sum(int(a) - int(b) for a, b in zip(s[:len(s)//2], s[::-1]))