# Lojban Numbers

"""
Counting in Lojban, an artificial language developed over the last forty years, is easier than in most languages. The numbers from zero to nine are:

1 pa 4 vo 7 ze
2 re 5 mu 8 bi 0 no
3 ci 6 xa 9 so
Larger numbers are created by gluing the digits together. For example, 123 is pareci.

Write a program that reads in a Lojban string (representing a number less than or equal to 1,000,000) and outputs it in numbers.

Example:
renonore  # Lojban string
2002  # Number

"""

# My Solution

def convert_lojban(lojban):
    lojban_vals = ['no', 'pa', 're', 'ci', 'vo' , 'mu', 'xa', 'ze', 'bi', 'so']
    loj_dict = dict(zip(lojban_vals, [i for i in range(0,10)]))
    lojban = [lojban[i:i+2] for i in range(0, len(lojban), 2)]
    
    return int(''.join([str(loj_dict[key]) for key in lojban]))


# Other Solutions

LOJBAN = {'no': '0', 'pa': '1', 're': '2', 'ci': '3', 'vo': '4', 'mu': '5', 'xa': '6', 'ze': '7', 'bi': '8', 'so': '9'}


def convert_lojban(lojban: str) -> int:
    return int(''.join(LOJBAN[lojban[i:i + 2]] for i in range(0, len(lojban), 2)))