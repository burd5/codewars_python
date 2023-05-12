# def collatz(number):
#     if number % 2 == 0:
#         print(number // 2)
#         return(number // 2)
#     else:
#         print(3 * number + 1)
#         return(3 * number + 1)

# try:
#     value = int(input('Pick a number:'))
#     value = collatz(value)
#     while value != 1:
#         value = collatz(value)
# except ValueError:
#     print('Nums only plz')

# Chapter 4 Practice Programs

# Comma Code

def comma_space(list):
    string = ''
    for i, word in enumerate(list):
        if word == list[-1]:
            string += f'and {word}'
        else:
            string += f'{word}, '
    return string

print(comma_space(['apples', 'bananas', 'tofu', 'cats']))

# Coin Flip Streaks
import random

def coin_streak():
    num_of_streaks = 0
    for i in range(10000):
        list = []
        for i in range(100):
            if random.randint(0,1) == 0: list.append('H')
            else: list.append('T')
        list = ''.join(list)
        if 'HHHHHH' in list or 'TTTTTT' in list:
            num_of_streaks += 1

    return(f'Chance of streak: {num_of_streaks/100}')

print(coin_streak())

# alternate coin flip solution
def coin_flips():
    # Code that creates a list of 100 'heads' or 'tails' values
    flips   = "".join(random.choice('HT') for _ in range(100))

    # Code that checks if there is a streak of 6 heads or tails in a row
    if 'HHHHHH' in flips or 'TTTTTT' in flips:
        number_of_streaks +=1

# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(6):
    for j in range(9):
        if j < 8:
            print(grid[j][i], end='')
        else: print(grid[j][i])