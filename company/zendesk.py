"""
Write an `encrypt` and a `decrypt` method. Each should accept a `key` and a `message`.

encrypt(key, message) should reorder the alphabet by moving the key's letters to the front. Then, it should return a string with the message's letters swapped out for their index in the new alphabet. Assume that the key will not contain the same letter more than once. 

For example, if your key is "things", the alphabet would transform this way:

Normal Alphabet:  abcdefghijklmnopqrstuvwxyz
New Alphabet:     thingsabcdefjklmopqruvwxyz

To encrypt your message, find each letter in the normal alphabet, and swap it out for the letter at the same index in the new alphabet. 

For example, if your message is "these are some words" the encrypt method would return "rbgqg tpg qljg wlpnq". 

encrypt("things", "these are some words")
=> "rbgqg tpg qljg wlpnq"


Decrypt just reverses the process:

decrypt("things", "rbgqg tpg qljg wlpnq")
=> "these are some words"


Use any language you like. Google any documentation you want, but no complete solutions. You're encouraged to ask clarifying questions.

Prioritize a complete solution first. We're most interested in the readability and completeness of your solution, and much less concerned with its performance.
"""


class Cipher:

    # class var for alpha
    def __init__(self):
        # self.new_alpha = self._new_alpha(key)
        pass

    def _new_alpha(self, key):  # build this new alphabet
        """

        "things"


        """

        cipher = {}
        cipher2 = {}
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        alpha1 = list("abcdefghijklmnopqrstuvwxyz")

        new_alpha = []

        for char in key:
            index = alpha.index(char)
            new_alpha.append(alpha.pop(index))

        new_alpha = new_alpha + alpha

        for char1, char2 in zip(alpha1, new_alpha):
            cipher[char1] = char2
            cipher2[char2] = char1

        return cipher, cipher2

    def encrypt(self, key, message):
        new_msg = []
        key = self._new_alpha(key)[0]  # dictionary

        for _, char in enumerate(message):
            if char.isalpha():
                new_msg.append(key[char])

            else:
                new_msg.append(char)

        return "".join(new_msg)

    def decrypt(self, key, msg):
        new_msg = []
        key = self._new_alpha(key)[1]  # dictionary

        for _, char in enumerate(msg):
            if char.isalpha():
                new_msg.append(key[char])

            else:
                new_msg.append(char)

        return "".join(new_msg)


c = Cipher()
print(c.encrypt("things", "these are some words") == "rbgqg tpg qljg wlpnq")
print(c.encrypt("", "these are some words") == "these are some words")
print(c.decrypt("things", "rbgqg tpg qljg wlpnq") == "these are some words")
