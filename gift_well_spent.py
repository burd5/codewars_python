"""
You will get the value of the gift card c and a finite list of item values. You should return a pair of indices that correspond to values that add up to c:

buy(2,[1,1])       = [0,1]
buy(3,[1,1])       = None
buy(5,[5,2,3,4,5]) = [1,2]

"""

# my nested loop solution

def buy(x,arr):        
    indices = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == x and i != j:
                indices.append([i, j])
    return None if not indices else indices[0]

# similar solution but stop at first match

def buy(x,arr):        
    for i in range(len(arr)):
        for y in range(len(arr)):
            if i !=y:
                if arr[i]+arr[y]== x:
                    return [i,y]
                
