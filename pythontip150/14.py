
def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    if len(string1) != len(string2):
        return False
    count_dict = {}
    for char in string1:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    for char in string2:
        if char in count_dict:
            count_dict[char] -= 1
        else:
            return False
    for count in count_dict.values():
        if count != 0:
            return False
    return True

print(are_anagrams('Astronomer', 'Moon starer'))