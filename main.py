# to do:

def solve_anagram(anagram):
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().splitlines()
    
    anagram = sorted(anagram.lower())
    
    word_table = {}
    # to store words that we can use to look up words that can be made from a given set of letters
    for word in words:
        # tuples can be used in a dict
        sorted_word = tuple(sorted(word.lower()))
        if sorted_word in word_table:
            word_table[sorted_word].append(word)
        else:
            word_table[sorted_word] = [word]
    
    # try to find a valid word using the anagram
    # looks to see if sorted letters is a key in the word_table
    sorted_letters = tuple(anagram)
    if sorted_letters in word_table:
        return word_table[sorted_letters]
    else:
        return None


if __name__ == '__main__':
    
    test_case = ['tefon', 'sokik', 'niumem', 'siconu']
    real_words = []
    for word in test_case:
        solutions = solve_anagram(word)
        real_words.append(solutions)

    print(real_words)
    