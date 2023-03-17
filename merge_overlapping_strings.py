"""
This kata requires you to write a function which merges two strings together. It does so by merging the end of the first string with the start of the second string together when they are an exact match.

"abcde" + "cdefgh" => "abcdefgh"
"abaab" + "aabab" => "abaabab"
"abc" + "def" => "abcdef"
"abc" + "abc" => "abc"
NOTE: The algorithm should always use the longest possible overlap.

"abaabaab" + "aabaabab" would be "abaabaabab" and not "abaabaabaabab"

"""


# solutions

def merge_strings(first, second):
    start = 0
    stop = len(first)
    while True:
        if first[start:len(first)] == second[0:stop]:
            break
        else:
            start = start + 1
            stop = stop - 1
    return first[0: start] + second

