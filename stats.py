def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_count_per_character(file_contents):
    lowercase = file_contents.lower()
    character_dict = {}
    for i in range(0, len(lowercase)):
        if lowercase[i] in character_dict:
            character_dict[lowercase[i]] += 1
        else:
            character_dict[lowercase[i]] = 1
    return character_dict

def get_sorted_list(character_dict):
    sorted_list = []
    for char in character_dict:
        dict = {}
        dict["char"]=char
        dict["num"]= character_dict[char]
        sorted_list.append(dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]