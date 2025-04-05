def word_count(text):
    count = 0
    words = text.split() 
    for word in words:
        count += 1
    return count

def character_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count: 
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_sorted(char_dict):
    result = []
    for char, count in char_dict.items():
        result.append({"char": char, "count": count})
    return result


