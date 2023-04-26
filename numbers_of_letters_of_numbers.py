"""
If we write out the digits of "60" as English words we get "sixzero"; the number
of letters in "sixzero" is seven. The number of letters in "seven" is five. The
number of letters in "five" is four. The number of letters in "four" is four:
we have reached a stable equilibrium.

Note: for integers larger than 9, write out the names of each digit in a single 
word (instead of the proper name of the number in English). For example, write 
12 as "onetwo" (instead of twelve), and 999 as "nineninenine" (instead of nine 
hundred and ninety-nine).

For any integer between 0 and 999, return an array showing the path from that 
integer to a stable equilibrium:

Examples
numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]
numbersOfLetters(1) --> ["one", "three", "five", "four"]

"""

# my solution

def numbers_of_letters(n):
    # arr for number string values
    num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
                 'eight', 'nine']
    # split original number into arr of numbers
    num_arr = [int(x) for x in str(n)]
    # create word array to store words for each loop
    word_arr = []
    # establish string value of first number
    word = ''.join([num_words[num] for num in num_arr])
    
    # while the word != 'four', continue to create new string value based on word
    # length
    while word != 'four':
        word_arr.append(word)
        word_len = len(word)
        num_arr = [int(x) for x in str(word_len)]
        word = ''.join([num_words[num] for num in num_arr])
    # add 'four' to the list and return
    word_arr.append('four')
    
    return word_arr

# other solutions

NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", 
       "nine"]

def numbers_of_letters(n):
    s = ''.join(NUM[i] for i in map(int, str(n)))
    return [s] + (numbers_of_letters(len(s)) if len(s) != n else [])

collection = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
}

def numbers_of_letters(n):
    res = []
    while 'four' not in res:
        ns = ''.join( [ collection[int(i)] for i in str(n if len(res) < 1 else 
        len(ns)) ] )
        res.append(ns) 
    return res