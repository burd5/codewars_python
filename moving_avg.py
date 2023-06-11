"""
Given a list values of integers and an integer n representing size of the window, calculate and return the moving average.

When integer n is equal to zero or the size of values list is less than window's size, return None
"""
# my solution
def moving_average(values,n):
    left, right = 0, n
    avgs = []
    try:
        while right <= len(values):
            avgs.append(sum(values[left:right])/n)
            left += 1
            right += 1
        
        return None if n > len(values) else avgs
    except:
        return None
    
    # shorter solution using list comprehension

def moving_average(a, n):
    if 0 < n <= len(a): 
        return [sum(a[i:i+n]) / n for i in range(len(a) - n + 1)]