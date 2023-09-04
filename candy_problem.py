# Candy Problem

"""
Your job is to find out how much candy each child has, and give them each additional candy until they too have as much as the child(ren) with the most candy. You also want to keep a total of how much candy you've handed out because reasons."

Your job is to give all the kids the same amount of candies as the kid with the most candies and then return the total number candies that have been given out. If there are no kids, or only one, return -1.

In the first case (look below) the most candies are given to second kid (i.e second place in list/array), 8. Because of that we will give the first kid 3 so he can have 8 and the third kid 2 and the fourth kid 4, so all kids will have 8 candies.So we end up handing out 3 + 2 + 4 = 9.

candies ([5,8,6,4]) # return 9

candies ([1,2,4,6]) # return 11

candies ([1,6]) # return 5

candies ([]) # return -1

candies ([6]) # return -1 (because only one kid)

"""

# My Solution

def candies(s):
    return -1 if not s or len(s) == 1 else len(s) * max(s) - sum(s)

# Other Solutions

def candies(s):
    return sum([max(s) - x for x in s]) if len(s) > 1 else -1

# Similar but more readable

def candies(s):
    if not s or len(s) == 1:
        return -1
    return len(s) * max(s) - sum(s)