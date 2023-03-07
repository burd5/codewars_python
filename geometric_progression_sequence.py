"""
In your class, you have started lessons about geometric progression. Since you are also a programmer, you have decided to write a function that will print first n elements of the sequence with the given constant r and first element a.

Result should be separated by comma and space.

Example
geometric_sequence_elements(2, 3, 5) == '2, 6, 18, 54, 162'

"""
def geometric_sequence_elements(a, r, n):
    answer = [a]
    for i in range(1, n):
        answer.append(answer[-1] * r)
    
    return ', '.join(map(str, answer))

# more efficient solution

def geometric_sequence_elements(a, r, n):
    return ", ".join(str(a * r**i) for i in range(n))