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