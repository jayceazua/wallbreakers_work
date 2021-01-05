# Counter automatically converts an iterable into a histogram
from collections import Counter
'''

You are running a classroom and suspect that some of your students are passing around the answers to multiple choice questions disguised as random strings.

Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled up inside the string, if any exists. There will be at most one matching word. The letters don't need to be contiguous.

Example:
words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
find_embedded_word(words, string1) -> cat

string2 = 'tbcanihjs'
find_embedded_word(words, string2) -> cat

string3 = 'baykkjl'
find_embedded_word(words, string3) -> None / null

string4 = 'bbabylkkj'
find_embedded_word(words, string4) -> baby

string5 = 'ccc'
find_embedded_word(words, string5) -> None / null

string6 = 'breadmaking'
find_embedded_word(words, string6) -> bird

W = number of words in `words`
L = maximal string length of each word

'''


words = ['baby', 'dog', 'bird', 'car', 'ax', 'cat']
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"


def find_embedded_word(words, string):
    if not words or not string:
        return None
    for word in words:  # O(n)
        if len(words) < len(string):  # checks if the word's length is greater than the given string
            # check each word in here if the word is in the given string
            if is_word_found(word, string):
                return word
    return None


def is_word_found(word, string):
    """ 
    {
        't': 1,
        'c': 1,
        'a': 1,
        'b': 1,
        'n': 1,
        ... n-1
    }
    histo = {}
    for letter in string:
        if letter not in histo:
            histo[letter] = 1
        else:
            histo[letter] += 1
    return histo
    """
    histo_word = Counter(word)
    histo_string = Counter(string)
    histo_word -= histo_string
    return len(histo_word) == 0


if __name__ == "__main__":
    print(find_embedded_word(words, string1))
    print(find_embedded_word(words, string2))
    print(find_embedded_word(words, string3))
    print(find_embedded_word(words, string4))
    print(find_embedded_word(words, string5))
    print(find_embedded_word(words, string6))
