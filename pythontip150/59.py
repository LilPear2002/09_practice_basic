
def count_consonants(word):
    # 在此处编写你的代码
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in word:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in word:
        if char.isalpha() and char.lower() in vowels:
            count += 1
    return count