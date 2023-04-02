"""
Oh no! Someone left the server at your local car dealership too close to a blender and now all of their data is scrambled.

It is your job to unscramble the data and put it into an easy to read dictionary.

Unscramble the list you are given and return the values in a dictionary such as the following:

dictionary = {'make': make, 'model': model, 'year': year, 'new': new}
You will be given a list containing a string (the make of the car), a tuple containing two strings (the model and sub-model), an integer (the year the car was manufactured) and a boolean (whether the car is new or used 'True' or 'False'), but you will not know the order of the list.

Return the dictionary where 'make' is a String, 'model' is a String, 'year' is an integer, and 'new' is a boolean of whether it is new (True) or used (False)

"""
# my solution

def make_model_year(lst):
    dict = {
       'make': '',
       'model': '',
       'year': '',
       'new': ''
    }
    for item in lst:
        if type(item) is tuple:
            dict['model'] = ' '.join(item)
        elif type(item) is int:
            dict['year'] = item
        elif item == True or item == False:
            dict['new'] = item
        else:
            dict['make'] = item
    
    return dict

# similar idea, different syntax

def make_model_year(lst):
    result = {}
    for item in lst:
        if isinstance(item, bool):
            result["new"] = item
        elif isinstance(item, int):
            result["year"] = item
        elif isinstance(item, tuple):
            result["model"] = " ".join(item)
        elif isinstance(item, str):
            result["make"] = item
    return result

# other solution

def make_model_year(lst):
    new, year, make, model = sorted(lst, key=lambda i: str(type(i)))
    return {'make':make, 'model':' '.join(model), 'year':year, 'new':new}