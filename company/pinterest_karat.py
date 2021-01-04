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


words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"


def find_embedded_word(words, string):

    for word in words:
        if found_word(word, string):
            return word
    return None


def found_word(word, string):
    # hist_word = Counter(word)
    hist_string = Counter(string)
    # hist_word -= hist_string
    # return True if len(hist_word) == 0 else False

    for letter in word:
        if not hist_string.get(letter):
            return False

        hist_string[letter] -= 1

        if hist_string[letter] <= 0:
            del hist_string[letter]

    return True


if __name__ == "__main__":
    print(find_embedded_word(words, string1))  # -> cat
    print(find_embedded_word(words, string2))
    print(find_embedded_word(words, string3))
    print(find_embedded_word(words, string4))
    print(find_embedded_word(words, string5))
    print(find_embedded_word(words, string6))
