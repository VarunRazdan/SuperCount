def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        if char.isalpha():
            char_info = {"char": char, "num": count}
            sorted_list.append(char_info)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    
