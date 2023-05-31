"""
#Get the averages of these numbers

Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.

Example:

Input:  [ 1, 3, 5, 1, -10]
Output:  [ 2, 4, 3, -4.5]
If the array has 0 or 1 values or is null, your method should return an empty array.

"""

def averages(arr):
    if arr == None: return []
    avg = []
    for i in range(len(arr) - 1):
        avg.append((arr[i + 1] + arr[i])/2)
            
    return [] if len(arr) < 2 else avg

# simplified solution

def averages(arr):
    return [(arr[x]+arr[x+1])/2 for x in range(len(arr or [])-1)]

# try catch solution

def averages(arr):
    output = []
    try:        
        for i in range(len(arr)-1):
            output.append( (arr[i]+arr[i+1]) / 2 )        
        return output
    
    except:
        return output