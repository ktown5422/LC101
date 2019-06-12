import string

def alphabet_position(letter):
    
    if letter in string.ascii_uppercase:
        position = string.ascii_uppercase.find(letter)
        
    elif letter in string.ascii_lowercase:
        position = string.ascii_lowercase.find(letter)
        
    return position

def rotate_character(char,rot):
    
    if char in string.ascii_uppercase:
        newChar = string.ascii_uppercase[(alphabet_position(char)+rot)%26]
    elif char in string.ascii_lowercase:
        newChar = string.ascii_lowercase[(alphabet_position(char)+rot)%26]
    else:
        newChar = char 
    
    return newChar 