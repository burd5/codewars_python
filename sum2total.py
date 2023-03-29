"""
Write a function that takes an array/list of numbers and returns a number such that

Explanation total([1,2,3,4,5]) => 48

1+2=3--\ 3+5 =>     8 \
2+3=5--/ \            ==  8+12=>20\     
          ==>5+7=> 12 / \           20+28 => 48
3+4=7--\ /            == 12+16=>28/
4+5=9--/ 7+9 =>     16  /

if total([1,2,3]) => 8 then

first+second => 3 \
                   then 3+5 => 8
second+third => 5 /

"""

# my solution

def total(arr):
    new_arr = arr
    while len(new_arr) != 1:
        temp_arr = []
        for i in range(len(new_arr) - 1):
            temp_arr.append(new_arr[i] + new_arr[i + 1])
        new_arr = temp_arr
    return new_arr[0]


# recursvie function

def total(xs):
    return xs[0] if len(xs) == 1 else total([xs[i] + x for i, x in enumerate(xs[1:])])