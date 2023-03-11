"""

Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.

Example:
"789" -> "123"

Notes:
You get a string with numbers only

"""

# my solution using make trans

def computer_to_phone(numbers):
    x = {'1': '7', '2': '8', '3': '9', '7': '1', '8': '2', '9': '3'}
    
    convert_table = str.maketrans(x)
    
    return numbers.translate(convert_table)

# more efficient way of using maketrans()

def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))