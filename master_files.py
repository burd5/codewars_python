"""
Are you a file extension master? Let's find out by checking if Bill's files are images or audio files. Please use regex if available natively for your language.

You will create 2 string methods:

isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .mp3, .flac, .alac, or .aac.

isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .jpg, .jpeg, .png, .bmp, or .gif.

Note that this is not a generic image/audio files checker. It's meant to be a test for Bill's files only. Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only

Rules

It should return true or false, simply.
File extensions should consist of lowercase letters and numbers only.
File names should consist of letters only (uppercase, lowercase, or both)

"""

# solutions

def is_audio(filename):
    name, ext = filename.split('.')
    return name.isalpha() and ext in {'mp3', 'flac', 'alac', 'aac'}


def is_img(filename):
    name, ext = filename.split('.')
    return name.isalpha() and ext in {'jpg', 'jpeg', 'png', 'bmp', 'gif'}

import re
def is_audio(file_name):
    return bool(re.match(r'^[A-Za-z]+\.(mp3|flac|alac|aac)$', file_name))

def is_img(file_name):
    return bool(re.search(r'^[A-Za-z]+\.(jpg|jpeg|png|bmp|gif)$', file_name))