"""
We all love the future president (or Führer or duce or sōtō as he could find 
them more fitting) donald trump, but we might fear that some of his many fans 
like John Miller or John Barron are not making him justice, sounding too much 
like their (and our as well, of course!) hero and thus risking to compromise him.

For this reason we need to create a function to detect the original and unique 
rhythm of our beloved leader, typically having a lot of extra vowels, all ready 
to fight the establishment.

The index is calculated based on how many vowels are repeated more than once in 
a row and dividing them by the total number of vowels a petty enemy of America 
would use.

For example:

trump_detector("I will build a huge wall")==0 #definitely not our trump: 0 on 
the trump score
trump_detector("HUUUUUGEEEE WAAAAAALL")==4 #4 extra "U", 3 extra "E" and 5 extra
 "A" on 3 different vowel groups: 12/3 make for a trumpy trumping score of 4: 
 not bad at all!
trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT")==1.56 #14 
extra vowels on 9 base ones

"""

def trump_detector(trump_speech):
    # counter to keep track of number of vowels
    vowels = 'aeiouAEIOU'
    num_of_vowels = 0
    # dict to keep track number of times each value appears
    dict = {}
    # for loop to loop through string and count vowels and number of occurences
    for letter in trump_speech:
        if letter in dict:
            dict[letter] += 1
        elif letter in vowels:
            dict[letter] = 1
            num_of_vowels += 1
    return len(dict.keys())/num_of_vowels