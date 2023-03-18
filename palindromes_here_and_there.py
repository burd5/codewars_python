"""


"""

# my solution

def convert_palindromes(numbers):
    answer_arr = [];
    for number in numbers:
        if is_palindrome(str(number)):
            answer_arr.append(1)
        else:
            answer_arr.append(0)
    return answer_arr

    
def is_palindrome(number):
    return number[::-1] == number

# more concise solution

def convert_palindromes(numbers):
    return [int(str(n) == str(n)[::-1]) for n in numbers]
