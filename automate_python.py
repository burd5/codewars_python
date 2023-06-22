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
"""
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
"""
# Character Picture Grid

""" 
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


theBoard = {
    'top-L': ' ',
    'top-M': ' ',
    'top-R': ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'low-L': ' ',
    'low-M': ' ',
    'low-R': ' '
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

"""

# Chess Dictionary Validator
"""
def isValidChessBoard(dict):
    keys = '1a1b1c1d1e1f1g1h2a2b2c2d2e2f2g2h3a3b3c3d3e3f3g3h4a4b4c4d4e4f4g4h\
    5a5b5c5d5e5f5g5h6a6b6c6d6e6f6g6h7a7b7c7d7e7f7g7h8a8b8c8d8e8f8g8h'

    white = {
        'pieces': 0,
        'pawn': 0,
        'rook': 0,
        'bishop': 0,
        'knight': 0,
        'king': 0,
        'queen': 0
    }

    black = {
        'pieces': 0,
        'pawn': 0,
        'rook': 0,
        'bishop': 0,
        'knight': 0,
        'king': 0,
        'queen': 0
    }

    for k,v in dict.items():
        key_vals = []
        if k in key_vals: return False
        key_vals.append(k)
        # key value is not a valid square
        if k not in keys: return False
        # value starts with a w
        elif v[0] == 'w':
            pieces += 1
            if white['pieces'] > 16 or \
            white['pawn'] > 8 or \
            white['rook'] > 2 or \
            white['bishop'] > 2 or \
            white['knight'] > 2 or \
            white['king'] > 1 or \
            white['queen'] > 1: return False
            if 'pawn' in v:
                white['pawn'] += 1
            elif 'rook' in v:
                white['rook'] += 1
            elif 'bishop' in v:
                white['bishop'] += 1
            elif 'knight' in v:
                white['knight'] += 1
            elif 'queen' in v:
                white['queen'] += 1
            elif 'king' in v:
                white['king'] += 1

        # value starts with a b
        elif v[0] == 'b':
            pieces += 1
            if black['pieces'] > 16 or \
            black['pawn'] > 8 or \
            black['rook'] > 2 or \
            black['bishop'] > 2 or \
            black['knight'] > 2 or \
            black['king'] > 1 or \
            black['queen'] > 1: return False
            if 'pawn' in v:
                black['pawn'] += 1
            elif 'rook' in v:
                black['rook'] += 1
            elif 'bishop' in v:
                black['bishop'] += 1
            elif 'knight' in v:
                black['knight'] += 1
            elif 'queen' in v:
                black['queen'] += 1
            elif 'king' in v:
                black['king'] += 1
        
        # value did not start with w or b so must be an error
        else: return False
    # return True if no errors are found
    return True


# Fantasy Game Inventory

def displayInventory(inventory):
    print('Inventory:')
    item_count = 0
    for k,v in inventory.items():
        item_count += v
        print(f'{inventory[k]} {k}')
    print(f'Total number of items: ' + str(item_count))

print(displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}))

def addToInventory(inventory, addedItems):
    inv = inventory
    for item in addedItems:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1

    return inv

inventory = addToInventory({'gold coin': 42, 'rope': 1}, ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])

displayInventory(inventory)

"""

# Multi-Clipboard Automatic Messages

