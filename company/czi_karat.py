"""
Your friends are now complaining that it's too hard to make sure the lengths of their status updates are not prime numbers.
You decide to create a substitution cipher. The cipher alphabet is based on a key shared amongst those of your friends who don't mind spoilers.
Suppose the key is:
"The quick onyx goblin, grabbing his sword, jumps over the lazy dwarf!". 
We use only the unique letters in this key to set the order of the characters in the substitution table.
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F
(spaces added for readability)
We then align it with the regular alphabet:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F
Which gives us the substitution table: A becomes T, B becomes H, C becomes E, etc.
Write a function that takes a key and a string and encrypts the string with the key.
Example:
key = "The quick onyx goblin, grabbing his sword, jumps over the lazy dwarf!"
encrypt("It was all a dream.", key) -> "Od ptw txx t qsutg."
"""

class Cipher:
  def __init__(self, key):
    self.cipher = self._alpha_cipher(key)

  @staticmethod
  def _alpha_cipher(key):
    cipher = {}
    for index, letter in enumerate(key):
      cipher[chr(ord('A') + index)] = letter
    return cipher

  @staticmethod
  def encrypt(message, key):
    new_msg = []
    for _, char in enumerate(message):
      if char.isalpha():
        if char.isupper():
          new_msg.append(key[char])

        else:
          letter = key[char.upper()]
          new_msg.append(letter.lower())

      else:
        new_msg.append(char)

    return "".join(new_msg)

    
c = Cipher("THEQUICKONYXGBLRASWDJMPVZF")
print(c.encrypt("It was all a dream.", c.cipher))
# ====================================================

"""
Route Cipher

"Dumbledore dies." -> "Dlriueeemd sbod."
r = 4
c = 4

[
  [D, u, m, b],
  [l, e, d, o],
  [r, e, , d],
  [i, e, s, .]
]

"Dlriueeemd sbod."

message2 = "Darth Vader was Luke's father." -> D r 'taV Lshrawu etdakfrhesea.
r2 = 6
c2 = 5
D r 'taV Lshrawu etdakfrhesea.
r3 = 5
c3 = 6
DVwkaaaaetrds'hte sehrL r  uf.
"""

message1 = "Dumbledore dies."
r1 = 4
c1 = 4
message2 = "Darth Vader was Luke's father."
r2 = 6
c2 = 5
r3 = 5
c3 = 6

def route_cipher(message, r, c):
    if not message:
        return
    # O(r * c) runtime; space complexity O(n)
    msg = build_matrix(message, r, c)
    # generate the new cipher message
    return get_new_message(msg)


def build_matrix(msg, r, c):
    """
    """
    msg_matrix = []
    msg_index = 0
    for i in range(r):
        msg_matrix.append([])
        for j in range(c):
            msg_matrix[i].append(msg[msg_index])
            msg_index += 1
    return msg_matrix


def get_new_message(matrix):
    s = []  # O(n)
    r = len(matrix)
    c = len(matrix[0])
    i = 0
    j = 0
    while j < c:
        if i == r:
            i = 0
            j += 1
        else:
            s.append(matrix[i][j])
            i += 1
    return "".join(s)  # O(n) runtime and space

