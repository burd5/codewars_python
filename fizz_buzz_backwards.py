"""
Traditionally in FizzBuzz, multiples of 3 are replaced by "Fizz" and multiples 
of 5 are replaced by "Buzz". But we could also play FizzBuzz with any other 
integer pair [n, m] whose multiples are replaced with Fizz and Buzz.

For a sequence of numbers, Fizzes, Buzzes and FizzBuzzes, find the numbers 
whose multiples are being replaced by Fizz and Buzz. Return them as an array [n, m]

The Fizz and Buzz numbers will always be integers between 1 and 50, and the 
sequence will have a maximum length of 100. The Fizz and Buzz numbers might be 
equal, and might be equal to 1.

Examples
Classic FizzBuzz; multiples of 3 are replaced by Fizz, multiples of 5 are 
replaced by Buzz:
[1, 2, "Fizz", 4, "Buzz", 6]  ==>  [3, 5] 
Multiples of 2 are replaced by Fizz, multiples of 3 are replaced by Buzz:
[1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]  ==>  [2, 3]
Multiples of 2 are replaced by Fizz and Buzz:
[1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]  ==>  [2, 2]
Fizz = 1, Buzz = 6:
["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]  ==>  [1, 6]

"""

# my solution

def reverse_fizz_buzz(array):
    # store indexes of Fizz and Buzz
    fizz = [i + 1 for i,x in enumerate(array) if x == 'Fizz']
    buzz = [i + 1 for i,x in enumerate(array) if x == 'Buzz']
    fizzBuzz = [i + 1 for i,x in enumerate(array) if x == 'FizzBuzz']
    # conditonal to report
    if fizz and buzz: return (fizz[0], buzz[0])
    if len(fizz) == 0 and len(buzz) == 0: return (fizzBuzz[0], fizzBuzz[0])
    if fizz and len(buzz) == 0: return (fizz[0], fizzBuzz[0])
    if len(fizz) == 0 and buzz: return (fizzBuzz[0], buzz[0])

# better solution

def reverse_fizz_buzz(array):
    fizz = array.index("Fizz") if "Fizz" in array else array.index("FizzBuzz")
    buzz = array.index("Buzz") if "Buzz" in array else array.index("FizzBuzz")
    return (fizz+1, buzz+1)

