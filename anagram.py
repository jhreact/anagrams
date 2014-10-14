"""
An anagram is a word formed by rearranging the letters of another, like
"topside" and "deposit". In some cases, there might be as many (or more)
anagrams than there are characters, like "post", "spot", "stop" and "tops".

Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and at least as many anagrams as there are letters.

The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/s hare/dict/words.

Your output should be in this format:

emit, item, mite, time
merit, miter, mitre, remit, timer
reins, resin, rinse, risen, serin, siren
inert, inter, niter, retin, trine
inset, neist, snite, stein, stine, tsine
"""

import string
DEBUG = False

# NOTE: reference implementation implies case-sensitivity
def get_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        word = word.strip()
        if len(word) >= 4:
            # convert to tuple so it's hashable
            chars = tuple(sorted([char for char in word if char in string.letters]))
            anagrams[chars] = anagrams.get(chars, [])
            anagrams[chars].append(word)
    return [anagram_list for (key_chars, anagram_list) in anagrams.items()
            if len(anagram_list) >= len(key_chars)]

def main():
    with open('words', 'r') as corpus:
        found_anagrams = get_anagrams(corpus)
        for anagrams in found_anagrams:
            print ', '.join(anagrams)

def test_anagrams():
    # make sure we only count letters
    test_words = ['emit', 'item', 'mit', 'mite', 'mitre', 'time', 'tea',
                  'eat', 'ate', 'eta', 'abc ', 'acb ', 'bca ', 'cab ', 'cba ']
    test_anagrams = get_anagrams(test_words)
    assert(len(test_anagrams) == 1)
    assert(len(test_anagrams[0]) >= len(test_anagrams[0][0]))
    assert(test_anagrams == [['emit', 'item', 'mite', 'time']])
    print "tests passed"


if __name__ == '__main__':
    if DEBUG:
        test_anagrams()
    main()

