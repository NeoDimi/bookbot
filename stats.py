def count_words(text: str) -> int:
    #Counts the number of words in a given text.
    words = text.split()
    return len(words)

def count_characters(text:str) -> dict:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def list_dict_characters(chars:dict) -> list:
    list_char_dicts = []
    for char in chars:
        char_dict ={
            "name": char,
            "count": chars[char]
        }
        list_char_dicts.append(char_dict)
    return list_char_dicts

def sort_on(dict:dict):
    return dict["count"]

def sort_list(list_dict:list) -> list:
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
#.sort() is an "in-place method" meaning it replaces what is has been given as input and returns a type "None".
#This is why we cannot store the result of .sort() in a new variable. It automatically erased its input with the output.