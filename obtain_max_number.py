# Obtain Max Number - Codewars 6kyu

"""
CodeBots decided to make a gift for CodeMaster's birthday. They got a pack of candies of various sizes from the store, but instead of giving the whole pack they are trying to make the biggest possible candy from them. On each turn it is possible:

to pick any two candies of the same size and merge
them into a candy which will be two times bigger;

to pick a single candy of an even size and split it 
into two equal candies half of this size each.```
What is the size of the biggest candy they can make as a gift?

# Example

For `arr = [2, 4, 8, 1, 1, 15]`, the output should be 16.
[2, 4, 8, 1, 1, 15] --> [2, 4, 8, 2, 15] -->[4, 4, 8, 15] --> [8, 8, 15] --> [16, 15] -->choose 16

"""

# My attempt

# Function to find highest combination of duplicates
def find_highest_combo(arr):
    dict = {}
    for num in arr:
        dict[num] = 1 + dict.setdefault(num, 0)
    highest = max([k if v >= 2 else 0 for k,v in dict.items()])
    return highest

# Function to find highest value when splitting even number
def find_highest_split(arr):
    print(arr)
    highest = max([x for x in arr if x % 2 == 0])
    return highest


def obtain_max_number(arr):
    while find_highest_combo(arr) or find_highest_split(arr):
        if find_highest_combo(arr) > find_highest_split(arr):
            new_val = find_highest_combo(arr) * 2
            arr = arr.remove(find_highest_combo(arr), 2)
            arr.append(new_val)
        elif find_highest_combo(arr) < find_highest_split(arr):
            new_vals = [find_highest_split(arr)/2] * 2
            arr.append(new_vals)
            arr = arr.remove(find_highest_split(arr))
    return max(arr)
        
# Solution

def obtain_max_number(arr):
    last_len = 0
    while len(arr) != last_len:
        last_len = len(arr)
        for n in arr:
            if arr.count(n) > 1:
                arr.remove(n)
                arr.remove(n)
                arr.append(n*2)
    
    return max(arr)