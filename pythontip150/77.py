
def letter_indices(word):
    return {letter: [i for i, char in enumerate(word) if char == letter] for letter in word}