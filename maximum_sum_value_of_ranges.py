# The maximum sum value of ranges -- Simple version

"""
 Given arr = [1,-2,3,4,-5,-4,3,2,1], 
       range = [[1,3],[0,4],[6,8]]
 should return 6
 
 calculation process:
 range[1,3] = arr[1]+arr[2]+arr[3] = 5
 range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
 range[6,8] = arr[6]+arr[7]+arr[8] = 6
 So the maximum sum value is 6
Note:
arr/$a always has at least 5 elements;
range/$range/ranges always has at least 1 element;
All inputs are valid;
This is a simple version, if you want some challenge, please try the challenge version.
Some Examples
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3],[0,4],[6,8]]) === 6
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3]]) === 5
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,4],[2,5]]) === 0

"""

# Simplified version

def max_sum(arr, ranges):
    return max( sum(arr[start:stop+1]) for start, stop in ranges )

# My solution

def max_sum(arr,ranges):
    maximum = float('-inf')
    for a in ranges:
        arr1 = a[0]
        arr2 = a[1] + 1 
        if a[1] != len(arr):
            maximum = max( (sum(arr[arr1:arr2])), maximum)
        else:
            maximum = max( (sum(arr[arr1:])), maximum)
            
    return maximum

