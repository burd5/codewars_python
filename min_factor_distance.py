# Min Factor Distance

"""
Write a function that returns the smallest distance between two factors of a number. The input will always be a number greater than one.

Example:

13013 has factors: [ 1, 7, 11, 13, 77, 91, 143, 169, 1001, 1183, 1859, 13013]

Hence the asnwer will be 2 (=13-11)

"""
# My Solution

def min_distance(n):
    # Find all factors of n
    factors = [x for x in range(1, n + 1) if n % x == 0]
    
    # Find minimum difference between factors
    return min([abs((factors[i + 1]) - factors[i]) for i in range(len(factors) - 1)])

# Other Solution

def min_distance(n):
    x = [i for i in range(1,n+1) if n%i==0]
    return min(j-i for i,j in zip(x, x[1:]))