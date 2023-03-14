"""

In this Kata, you will be given a number, two indexes (index1 and index2) and a digit to look for. Your task will be to check if the digit exists in the number, within the indexes given.

Be careful, the index2 is not necessarily more than the index1.

  index1 == 2 and index2 == 5 -> snippet from 2 to 5 positons;
  index1 == 5 and index2 == 2 -> snippet from 2 to 5 positons;

  number.length = 14;
  
  0 <= index1 < 14;
  
  0 <= index2 < 14;
  
  index2 is inclusive in search snippet;
  
  0 <= digit <= 9;
Find more details below:


  checkDigit(12345678912345, 1, 0, 1) -> true, 1 exists in 12
  
  checkDigit(12345678912345, 0, 1, 2) -> true, 2 exists in 12

"""


# my solution

def check_digit(number, index1, index2, digit):
    number = str(number)
    sorted_nums = sorted([index1, index2])
    sub_string = number[sorted_nums[0]:sorted_nums[1] + 1]
    if str(digit) in sub_string:
        return True
    else:
        return False
    

# more efficient ways to write it

def check_digit(n, i1, i2, d):
    return str(d) in str(n)[min(i1,i2):max(i1,i2)+1]

def check_digit(n, idx1, idx2, digit):
    return str(digit) in str(n)[idx1:idx2+1] + str(n)[idx2:idx1+1]