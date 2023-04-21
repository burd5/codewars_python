"""
In this kata, you have an integer array which was ordered by ascending except 
one number.

For Example: [1,2,3,4,17,5,6,7,8]
For Example: [19,27,33,34,112,578,116,170,800]
You need to figure out the first breaker. Breaker is the item, when removed from
 sequence, sequence becomes ordered by ascending.

For Example: [1,2,3,4,17,5,6,7,8] => 17 is the only breaker.

For Example: [19,27,33,34,112,578,116,170,800] => 578 is the only breaker.

"""
# my solution

def order_breaker(input):
    for i, num in enumerate(input):
        # copy original list
        temp_list = input[:]
        # remove the current element that for loop index is on
        temp_list.pop(i)
        # if list is sorted without this element, we know it's the breaker and
        # we return it
        if temp_list == sorted(temp_list):
            return input[i]


print(order_breaker([-11, 5, 0, 3, 4]))
print(order_breaker([5, 7, 6, 8, 9, 10]))

# similar solution

def order_breaker(inp):
    for i, num in enumerate(inp):
        x = inp[0:i] + inp[i+1:]
        if x == sorted(x):
            return num