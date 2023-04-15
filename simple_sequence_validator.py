"""
Create a function that will return true if all numbers in the sequence follow the same counting pattern. If the sequence of numbers does not follow the same pattern, the function should return false.

Sequences will be presented in an array of varied length. Each array will have a minimum of 3 numbers in it.

The sequences are all simple and will not step up in varying increments such as a Fibonacci sequence.

JavaScript examples:

validateSequence([1,2,3,4,5,6,7,8,9]) === true
validateSequence([1,2,3,4,5,8,7,8,9]) === false
validateSequence([2,4,6,8,10]) === true

"""

# my solution

def validate_sequence(sequence):
    seq_step = sequence[1] - sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i + 1] - seq_step:
            return False
        
    return True

#