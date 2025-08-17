def count_words(booktext):
    return len(booktext.split())

def count_characters(booktext):
    characters = {}
    
    #booktext = booktext.lower().split()
    for word in booktext:  
        lowered = word.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    
    return characters

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    
    sorted = []
    
    for key in dict:
        num = {}
        num["name"] = key
        num["num"] = dict[key]
        sorted.append(num)
    
    sorted.sort(reverse=True, key=sort_on)
    return sorted