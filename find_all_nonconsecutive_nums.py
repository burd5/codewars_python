"""

Your task is to find all the elements of an array that are non consecutive.

A number is non consecutive if it is not exactly one larger than the previous element in the array. The first element gets a pass and is never considered non consecutive.

Create a function name all_non_consecutive

E.g., if we have an array [1,2,3,4,6,7,8,15,16] then 6 and 15 are non-consecutive.

You should return the results as an array of objects with two values i: <the index of the non-consecutive number> and n: <the non-consecutive number>.

E.g., for the above array the result should be:

[
  {'i': 4, 'n': 6},
  {'i': 7, 'n': 15}
]

"""

# my solution

def all_non_consecutive(arr):
    dict = []
    for ix in range(1, len(arr)):
        if arr[ix] != arr[ix - 1] + 1:
            dict.append({
                'i' : ix,
                'n' : arr[ix]  
            })          
    
    return dict

# concise answer using zip and enumerate

def all_non_consecutive(a):
    return [{"i": i, "n": y} for i, (x, y) in enumerate(zip(a, a[1:]), 1) if x != y - 1]

# similar answer to mine

def all_non_consecutive(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i + 1] - arr[i] != 1:
            answer.append({'i': i + 1, 'n': arr[i + 1]})
    return answer