"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE_CODE = [
            ".-",   # a -> 0
                    "-...",  # b -> 1
                    "-.-.",  # c -> 2
                    "-..",  # d -> 3
                    ".",    # e -> 4
                    "..-.",  # f -> 5
                    "--.",  # g -> 6
                    "....",  # h -> 7
                    "..",   # i -> 8
                    ".---",  # j -> 9
                    "-.-",  # k -> 10
                    ".-..",  # l -> 11
                    "--",   # m -> 12
                    "-.",   # n -> 13
                    "---",  # o -> 14
                    ".--.",  # p -> 15
                    "--.-",  # q -> 16
                    ".-.",  # r -> 17
                    "...",  # s -> 18
                    "-",    # t -> 19
                    "..-",  # u -> 20
                    "...-",  # v -> 21
                    ".--",  # w -> 22
                    "-..-",  # x -> 23
                    "-.--",  # y -> 24
                    "--.."  # z -> 25
        ]

        morse = set()
        conversion = ""
        for word in words:
            for letter in word:
                conversion += MORSE_CODE[ord(letter) - ord('a')]
            morse.add(conversion)
            conversion = ""

        return len(morse)
