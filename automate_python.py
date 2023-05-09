def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        print(3 * number + 1)
        return(3 * number + 1)

try:
    value = int(input('Pick a number:'))
    value = collatz(value)
    while value != 1:
        value = collatz(value)
except ValueError:
    print('Nums only plz')




