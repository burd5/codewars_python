"""
Maya writes weekly articles to a well known magazine, but she is missing one word each time she is about to send the article to the editor. The article is not complete without this word. Maya has a friend, Dan, and he is very good with words, but he doesn't like to just give them away. He texts Maya a number and she needs to find out the hidden word. The words can contain only the letter:

"a", "b", "d", "e", "i", "l", "m", "n", "o", and "t".

"""


# my solution
def hidden(num):
    key = {
    "a" : 6,
    "b" : 1 ,
    "d" : 7,
    "e" : 4,
    "i" : 3,
    "l" : 2,
    "m" : 9,
    "n" : 8,
    "o" : 0,
    "t" : 5,
}
    num = [int(x) for x in str(num)]
    keys = list(key.keys())
    values = list(key.values())
    word = ''
    for letter in num:
        index = values.index(letter)
        word += keys[index]
        
    return word

# other solutions

trans = dict(zip('6174329805','abdeilmnot'))

def hidden(num):
    return ''.join( trans[char] for char in str(num) )

def hidden(num):
    return str(num).translate(str.maketrans("6174329805", "abdeilmnot"))

def hidden(num):
    d = 'oblietadnm'
    return ''.join([d[int(i)] for i in str(num)])