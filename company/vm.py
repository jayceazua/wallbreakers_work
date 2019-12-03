"""
Compress String

input:
  'a12c9b56c1'

output:
  'a12b56c10'

"""

def compress_string(s):
  if not s:
    return s
  
  number = "" # O(n)
  chars = {}
  j = 0
  for index, char in enumerate(s): # O(n)

    if char.isalpha():
      j = index + 1
      # get integer
      while j < len(s) and not s[j].isalpha(): # O(i)
        number += s[j]
        j += 1

      num = int(number)
      # reset the integer
      number = ""
      
      if char in chars:
        chars[char] += num
      else:
        chars[char] = num
  
  s = ""
  letters = list(chars.keys())
  
  for letter in sorted(letters):
    s += letter + str(chars[letter])

  return s
  

print(compress_string('a12c9b56c1'))

