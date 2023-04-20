"""
You have to extract a portion of the file name as follows:

Assume it will start with date represented as long number
Followed by an underscore
You'll have then a filename with an extension
it will always have an extra extension at the end
Inputs:
1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION

1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34

1231231223123131_myFile.tar.gz2
Outputs
FILE_NAME.EXTENSION

This_is_an_otherExample.mpg

myFile.tar

"""

# my solution

import re
class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        first_part = re.search(r'(?<=\_).*(?=\.)', dirty_file_name)
        return first_part.group(0)
    
# other solution

class FileNameExtractor:
    def extract_file_name(f):
        return f[f.find("_")+1:f.rfind(".")]