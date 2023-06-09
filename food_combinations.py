# Code Wars 7kyu - Food Combinations

"""
Given an array containing a list of good foods, return a string containing the assertion that any two of the individually good foods are really good when combined.

eg: "You know what's actually really good? Pancakes and relish."

Examples:
Good_foods = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup", "Cheese", "Eggs", "Cupcakes", "Sour cream", "Hot chocolate", "Avocado", "Skittles"]

actually_really_good( Good_foods ) #  "You know what's actually really good? Pancakes and relish."

actually_really_good( ['Peanut butter'] ) #  "You know what's actually really good? Peanut butter and more peanut butter."

actually_really_good( [] ) #  "You know what's actually really good? Nothing!"

"""
# my solution
import random
def actually_really_good(foods):
    if len(foods) >= 2:
        food1 = random.choice(foods)
        foods.remove(food1)
        food2 = random.choice(foods)
        return f"You know what's actually really good? {food1.capitalize()} and {food2.lower()}."
    elif len(foods) == 1:
        return f"You know what's actually really good? {foods[0].capitalize()} and more {foods[0].lower()}."
    else:
        return f"You know what's actually really good? Nothing!"
    
# Cleaner code solutions

from random import sample


def actually_really_good(foods):
    question = "You know what's actually really good? "
    len_foods = len(foods)
    if len_foods == 0:
        return question + "Nothing!"
    elif len_foods == 1:
        food = foods[0]
        return question + f"{food.capitalize()} and more {food.lower()}."
    else:
        [food1, food2] = sample(foods, 2)
        return question + f"{food1.capitalize()} and {food2.lower()}."