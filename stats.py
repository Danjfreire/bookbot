def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}

    for c in text:
        lower_c = c.lower()
        if lower_c not in characters:
            characters[lower_c] = 0

        characters[lower_c] += 1

    return characters

def sort_on(items):
    return items["num"]

def sort_char_count(char_count):
    char_dicts = []
    for key, val in char_count.items():
        if not key.isalpha():
            continue
        char_dicts.append({"char": key, "num": val})
    
    char_dicts.sort(reverse=True, key=sort_on)

    return char_dicts
    

