def count_words(text: str) -> int:
    #Counts the number of words in a given text.
    words = text.split()
    return len(words)

def count_characters(text:str) -> dict:
    text_lower = text.lower()
    characters = {
        'a': text_lower.count('a'),
        'b': text_lower.count('b'),
        'c': text_lower.count('c'),
        'd': text_lower.count('d'),
        'e': text_lower.count('e'),
        'f': text_lower.count('f'),
        'g': text_lower.count('g'),
        'h': text_lower.count('h'),
        'i': text_lower.count('i'),
        'j': text_lower.count('j'),
        'k': text_lower.count('k'),
        'l': text_lower.count('l'),
        'm': text_lower.count('m'),
        'n': text_lower.count('n'),
        'o': text_lower.count('o'),
        'p': text_lower.count('p'),
        'q': text_lower.count('q'),
        'r': text_lower.count('r'),
        's': text_lower.count('s'),
        't': text_lower.count('t'),
        'u': text_lower.count('u'),
        'v': text_lower.count('v'),
        'w': text_lower.count('w'),
        'x': text_lower.count('x'),
        'y': text_lower.count('y'),
        'z': text_lower.count('z'),
        'à': text_lower.count('à'),
        'â': text_lower.count('â'),
        'ä': text_lower.count('ä'),
        'é': text_lower.count('é'),
        'è': text_lower.count('è'),
        'ê': text_lower.count('ê'),
        'ë': text_lower.count('ë'),
        'î': text_lower.count('î'),
        'ï': text_lower.count('ï'),
        'ô': text_lower.count('ô'),
        'ö': text_lower.count('ö'),
        'ù': text_lower.count('ù'),
        'û': text_lower.count('û'),
        'ü': text_lower.count('ü'),
        'ç': text_lower.count('ç'),
        'ñ': text_lower.count('ñ'),
        'ß': text_lower.count('ß'),
        'æ': text_lower.count('æ'),
        'œ': text_lower.count('œ')
        }
    return characters